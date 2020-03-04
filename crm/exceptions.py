from django.core.checks import Error


class DatabaseConnectionError(Error):

    def __init__(self, inner_exception: BaseException, obj):
        super().__init__(
            id='crm.E001',
            msg=str(inner_exception),
            hint='Please check database configuration.',
            obj=obj
        )
