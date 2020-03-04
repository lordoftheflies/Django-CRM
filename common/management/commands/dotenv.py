from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Create .crm file for dotenv configuration.
    """
    requires_system_checks = False
    help = 'Setup dotenv.'

    def add_arguments(self, parser):
        parser.add_argument('environment', type=str, default='staging', help='Choose environment.')

    def handle(self, *args, **options):
        try:
            import dotenv
            from os import path

            from crm import ENVIRONMENT_CONFIGURATION


            from django.conf import settings
            if not path.exists('.crm'):
                with open('.crm', 'w') as file:
                    file.write('# %s\n' % getattr(settings, '__doc__').replace('\n', '\n# '))
                    # file.write('KRYNEGGER_CONFIGURATION=%s\n' % str(options['environment']).lower())
                    settings_dict = dir(settings)
                    for key in settings_dict:
                        if key.isupper():
                            file.write('KRYNEGGER_%s=%s\n' % (key, getattr(settings, key)))
                self.stdout.write(self.style.SUCCESS('Successfully created dotenv file for "%s" configuration at ./.crm' % options['environment']))
        except BaseException as e:
            self.stdout.write(self.style.ERROR('Failed to create database'))
            self.stdout.write(self.style.ERROR(str(e)))