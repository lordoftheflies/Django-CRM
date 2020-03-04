import logging
import os
import sys

from configurations.wsgi import get_wsgi_application


PROJECT_DIR = os.path.abspath(__file__)
sys.path.append(PROJECT_DIR)

try:
    import os
    from dotenv import load_dotenv
    # explicitly providing path to '.env'
    from pathlib import Path  # python3 only
    env_path = Path('.') / '.crm'
    load_dotenv(dotenv_path=env_path)
    ENVIRONMENT_CONFIGURATION = os.getenv("DJANGO_CONFIGURATION", 'Development')
except BaseException as e:
    logging.error('Dotenv file could not loaded')
    # logging.exception(e)
    # traceback.print_exc()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")

application = get_wsgi_application()
