from __future__ import absolute_import, unicode_literals

import logging
import traceback

from django.core import checks
from django.core.checks import register, Tags

from .exceptions import DatabaseConnectionError

try:
    import os
    from dotenv import load_dotenv
    # explicitly providing path to '.env'
    from pathlib import Path  # python3 only
    env_path = Path('.') / '.crm'
    load_dotenv(dotenv_path=env_path)
    ENVIRONMENT_CONFIGURATION = os.getenv("KRYNEGGER_CONFIGURATION")
except BaseException as e:
    logging.error('Dotenv file could not loaded')
    # logging.exception(e)
    # traceback.print_exc()

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']

@register()
def database_check(app_configs, **kwargs):
    errors = []
    from django.db import connections
    from django.db.utils import OperationalError
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError as operational_exception:
        errors.append(DatabaseConnectionError(operational_exception, db_conn))
    finally:
        return errors