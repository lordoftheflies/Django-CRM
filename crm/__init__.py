from __future__ import absolute_import, unicode_literals

import logging
import traceback

from django.core import checks
from django.core.checks import register, Tags

# from .exceptions import DatabaseConnectionError



# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']

# @register()
# def database_check(app_configs, **kwargs):
#     errors = []
#     from django.db import connections
#     from django.db.utils import OperationalError
#     db_conn = connections['default']
#     try:
#         c = db_conn.cursor()
#     except OperationalError as operational_exception:
#         errors.append(DatabaseConnectionError(operational_exception, db_conn))
#     finally:
#         return errors