#!/usr/bin/env python
import logging
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crm.settings")
    # os.environ['DJANGO_SETTINGS_MODULE'] = "crm.settings"
    os.environ.setdefault("DJANGO_CONFIGURATION", 'Development')

    try:
        import os
        from dotenv import load_dotenv
        # explicitly providing path to '.env'
        from pathlib import Path  # python3 only
        env_path = Path('.') / '.crm'
        load_dotenv(dotenv_path=env_path)

    except BaseException as e:
        logging.error('Dotenv file could not loaded')
        # logging.exception(e)
        # traceback.print_exc()

    finally:
        ENVIRONMENT_CONFIGURATION = os.getenv("DJANGO_CONFIGURATION", 'Development')

    try:
        from configurations.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            pass

        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
