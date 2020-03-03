import logging
import os

import dj_database_url
from celery.schedules import crontab
from configurations import Configuration, values
from django.core import validators


class BasicConfiguration(Configuration):
    """
    Basic CRM configuration, which satisfying the [ISO-27001](https://google.com), [ISO-270018](https://google.com),
    [SOC:AICPAA](https://google.com), and  [HIPAA](https://google.com) standards.
    """

    DEBUG = values.BooleanValue(False)

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = values.PathValue(
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        check_exists=True,
        environ_prefix='KRYNEGGER'
    )

    SECRET_KEY = values.SecretValue(environ_prefix='KRYNEGGER')

    ALLOWED_HOSTS = [
        '*'
    ]

    # Application definition
    LOGIN_REDIRECT_URL = values.PathValue('/', check_exists=False,)
    LOGIN_URL = values.PathValue('/login/', check_exists=False,)

    INSTALLED_APPS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.messages',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'simple_pagination',
        'compressor',
        'haystack',
        'common',
        'accounts',
        'cases',
        'contacts',
        'emails',
        'leads',
        'opportunity',
        'planner',
        'sorl.thumbnail',
        'phonenumber_field',
        'storages',
        'marketing',
        'tasks',
        'invoices',
        'events',
        'teams',
    ]

    # Password validation
    # https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR.value, "templates"), ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    ROOT_URLCONF = 'crm.urls'
    WSGI_APPLICATION = 'crm.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'dj_crm',
    #         'USER': 'postgres',
    #         'PASSWORD': 'root',
    #         'HOST': os.getenv('DB_HOST', '127.0.0.1'),
    #         'PORT': os.getenv('DB_PORT', '5432')
    #     }
    # }
    DATABASES = values.DatabaseURLValue('postgres://krynegger:qwe123@localhost/krynegger_database', environ_prefix='KRYNEGGER')
    # DATABASES = dict(
    #     default=dj_database_url.config(
    #         env='KRYNEGGER_DATABASE_PRIMARY_URL',
    #         default='postgres://krynegger:qwe123@localhost/krynegger_database'
    #     )
    # )
    # Internationalization
    # https://docs.djangoproject.com/en/1.10/topics/i18n/

    LANGUAGE_CODE = values.Value('en-us', environ_prefix='KRYNEGGER')

    TIME_ZONE = values.Value('Europe/Budapest', environ_prefix='KRYNEGGER')

    USE_I18N = values.BooleanValue(True, environ_prefix='KRYNEGGER')

    USE_L10N = values.BooleanValue(True, environ_prefix='KRYNEGGER')

    USE_TZ = values.BooleanValue(True, environ_prefix='KRYNEGGER')

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
    # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # EMAIL_HOST = 'localhost'
    # EMAIL_PORT = 25
    # AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', )

    EMAIL_HOST = values.Value('aspmx.l.google.com', environ_prefix='KRYNEGGER')
    EMAIL_HOST_USER = values.Value('laszlo.hegedus@cherubits.hu', environ_prefix='KRYNEGGER')
    EMAIL_HOST_PASSWORD = values.Value('Armageddon43254325', environ_prefix='KRYNEGGER')
    EMAIL_PORT = values.IntegerValue(587, environ_prefix='KRYNEGGER')
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'no-reply@crm.cherubits.hu'

    AUTH_USER_MODEL = 'common.User'

    DEFAULT_S3_PATH = "media"
    AWS_STORAGE_BUCKET_NAME = AWS_BUCKET_NAME = os.getenv('AWSBUCKETNAME', '')
    AM_ACCESS_KEY = AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AM_PASS_KEY = AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    S3_DOMAIN = AWS_S3_CUSTOM_DOMAIN = str(AWS_BUCKET_NAME) + '.s3.amazonaws.com'

    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_IS_GZIPPED = True
    AWS_ENABLED = True
    AWS_S3_SECURE_URLS = True
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_S3_PATH = "static"
    COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_REGION = os.getenv('AWS_REGION', '')

    # Currently 'normal' and 's3' storage implemented.
    STORAGE_TYPE = values.Value('normal', environ_prefix='KRYNEGGER')

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.10/howto/static-files/
    @property
    def STATIC_ROOT(self):
        if self.STORAGE_TYPE == 's3':
            return "/%s/" % STATIC_S3_PATH
        else:
            return values.PathValue(
                default=os.path.join(self.BASE_DIR, 'static'),
                environ_name='STATIC_ROOT',
                environ_prefix='KRYNEGGER'
            )

    @property
    def STATIC_URL(self) -> str:
        if self.STORAGE_TYPE == 's3':
            return 'https://%s/' % (self.S3_DOMAIN)
        else:
            return values.Value(
                default='/static/',
                # check_exists=False,
                environ_name='STATIC_URL',
                environ_prefix='KRYNEGGER'
            )

    @property
    def STATICFILES_DIRS(self) -> list:
        if self.STORAGE_TYPE == 's3':
            return [self.BASE_DIR + '/static']
        else:
            return values.ListValue(
                default=[
                ],
                environ_name='STATICFILES_DIRS',
                environ_prefix='KRYNEGGER'
            )

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]

    @property
    def MEDIA_ROOT(self) -> str:
        if self.STORAGE_TYPE == 's3':
            return '/%s/' % self.DEFAULT_S3_PATH
        else:
            return values.PathValue(
                default=os.path.join(self.BASE_DIR, 'media'),
                environ_name='MEDIA_ROOT',
                environ_prefix='KRYNEGGER'
            )

    @property
    def MEDIA_URL(self) -> str:
        if self.STORAGE_TYPE == 's3':
            return '//%s/%s/' % (self.S3_DOMAIN, self.DEFAULT_S3_PATH)
        else:
            return values.Value(
                default='/media/',
                environ_name='MEDIA_URL',
                environ_prefix='KRYNEGGER'
            )

    @property
    def ADMIN_MEDIA_PREFIX(self) -> str:
        return self.STATIC_URL + 'admin/'

    COMPRESS_ROOT = values.PathValue(os.path.join(BASE_DIR.value, 'static'))

    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter'
    ]
    COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
    COMPRESS_REBUILD_TIMEOUT = 5400
    CORS_ORIGIN_ALLOW_ALL = True
    COMPRESS_ROOT = BASE_DIR.value + '/static/'
    COMPRESS_OUTPUT_DIR = 'CACHE'
    COMPRESS_URL = STATIC_URL
    COMPRESS_ENABLED = True
    COMPRESS_OFFLINE_CONTEXT = {
        'STATIC_URL': 'STATIC_URL',
    }
    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
        ('text/x-sass', 'sass {infile} {outfile}'),
        ('text/x-scss', 'sass {infile} {outfile}'),
    )

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.elasticsearch2_backend.Elasticsearch2SearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        },
    }

    HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

    HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

    PASSWORD_RESET_MAIL_FROM_USER = os.getenv('PASSWORD_RESET_MAIL_FROM_USER', 'no-reply@django-crm.com')


class MailConfigurationMixin(object):
    MAIL_SENDER = 'AMAZON'
    INACTIVE_MAIL_SENDER = 'MANDRILL'

    MGUN_API_URL = os.getenv('MGUN_API_URL', '')
    MGUN_API_KEY = os.getenv('MGUN_API_KEY', '')

    SG_USER = os.getenv('SG_USER', '')
    SG_PWD = os.getenv('SG_PWD', '')

    MANDRILL_API_KEY = os.getenv('MANDRILL_API_KEY', '')

    ADMIN_EMAIL = "admin@micropyramid.com"

    URL_FOR_LINKS = "http://demo.django-crm.io"

    GP_CLIENT_ID = os.getenv('GP_CLIENT_ID', False)
    GP_CLIENT_SECRET = os.getenv('GP_CLIENT_SECRET', False)
    ENABLE_GOOGLE_LOGIN = os.getenv('ENABLE_GOOGLE_LOGIN', False)

    MARKETING_REPLY_EMAIL = 'djangocrm@micropyramid.com'

    PASSWORD_RESET_TIMEOUT_DAYS = 3


class SentryConfigurationMixin(object):
    SENTRY_ENABLED = values.BooleanValue(False)

    @property
    def SENTRY_INSTALLED_APPS(self) -> list:
        return [
            'raven.contrib.django.raven_compat',
        ]

    @property
    def INSTALLED_APPS(self) -> list:
        if self.SENTRY_ENABLED:
            return super.INSTALLED_APPS + self.SENTRY_INSTALLED_APPS
        else:
            return super.INSTALLED_APPS

    def RAVEN_CONFIG(self) -> dict:
        return dict(dsn=os.getenv('SENTRYDSN', ''))

    @property
    def SENTRY_MIDDLEWARE(self):
        return [
            'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
            'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
        ]

    @property
    def MIDDLEWARE(self):
        if self.SENTRY_ENABLED:
            return super.MIDDLEWARE + self.SENTRY_MIDDLEWARE
        else:
            return super.MIDDLEWARE


class URIValue(values.ValidationMixin, values.Value):
    message = 'Cannot interpret URL value {0!r}'
    validator = validators.URLValidator(schemes=[
        'http', 'https',
        'ftp', 'ftps',
        'ldap', 'ldaps',
        'smtp', 'smtps',
        'redis',
        'postgres',
    ])

class CeleryConfiguration(object):
    # celery Tasks
    CELERY_BROKER_URL = URIValue('redis://localhost:6379')
    CELERY_RESULT_BACKEND = URIValue('redis://localhost:6379')

    CELERY_BEAT_SCHEDULE = {
        "runs-campaign-for-every-thiry-minutes": {
            "task": "marketing.tasks.run_all_campaigns",
            "schedule": crontab(minute=30, hour='*')
        },
        "runs-campaign-for-every-five-minutes": {
            "task": "marketing.tasks.list_all_bounces_unsubscribes",
            "schedule": crontab(minute='*/5')
        },
        "runs-scheduled-campaigns-for-every-one-hour": {
            "task": "marketing.tasks.send_scheduled_campaigns",
            "schedule": crontab(hour='*/1')
        },
        "runs-scheduled-emails-for-accounts-every-one-minute": {
            "task": "accounts.tasks.send_scheduled_emails",
            "schedule": crontab(minute='*/1')
        }
    }


class Development(BasicConfiguration, MailConfigurationMixin, CeleryConfiguration, SentryConfigurationMixin):
    """
    Development CRM configuration, for easy debugging and diagnosing.
    """

    DEBUG = values.BooleanValue(True)

    # SECURITY WARNING: keep the secret key used in production secret!
    # Set in local_settings.py
    SECRET_KEY = 'SECRET_SECRET_SECRET'

    @classmethod
    def pre_setup(cls):
        super(Development, cls).pre_setup()

    @classmethod
    def setup(cls):
        super(Development, cls).setup()
        logging.info('development settings loaded: %s', cls)

    @classmethod
    def post_setup(cls):
        super(Development, cls).post_setup()
        logging.debug("done setting up! \o/")


class Staging(BasicConfiguration, MailConfigurationMixin, CeleryConfiguration, SentryConfigurationMixin):
    """
    Staging CRM configuration, equal with development, but secure.
    """

    @classmethod
    def pre_setup(cls):
        super(Staging, cls).pre_setup()

    @classmethod
    def setup(cls):
        super(Staging, cls).setup()
        logging.info('staging settings loaded: %s', cls)

    @classmethod
    def post_setup(cls):
        super(Staging, cls).post_setup()
        logging.debug("done setting up! \o/")


class Production(Staging):
    """
    Production CRM configuration, secure and rmd.
    """
    DEBUG = False

    @classmethod
    def pre_setup(cls):
        super(Production, cls).pre_setup()

    @classmethod
    def setup(cls):
        super(Production, cls).setup()
        logging.info('production settings loaded: %s', cls)

    @classmethod
    def post_setup(cls):
        super(Staging, cls).post_setup()
        logging.debug("done setting up! \o/")
