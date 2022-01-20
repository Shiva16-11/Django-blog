from django.apps import AppConfig
#comments

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
