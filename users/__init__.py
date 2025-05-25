default_app_config = 'users.apps.UsersConfig'

# This will ensure that the custom user model is used
from django.conf import settings
settings.AUTH_USER_MODEL = 'users.User'