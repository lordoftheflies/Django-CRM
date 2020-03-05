from django.conf import settings
from storages.backends.ftp import FTPStorage


class StaticfilesFtpStorage(FTPStorage):

    def __init__(self):
        super().__init__(base_url=settings.STATIC_URL)