import os
import sys

from configurations.wsgi import get_wsgi_application

from crm import ENVIRONMENT_CONFIGURATION

PROJECT_DIR = os.path.abspath(__file__)
sys.path.append(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")
if ENVIRONMENT_CONFIGURATION:
    os.environ.setdefault('DJANGO_CONFIGURATION', ENVIRONMENT_CONFIGURATION.title())
else:
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

application = get_wsgi_application()
