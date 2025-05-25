"""
WSGI config for yut_backend project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yut_backend.settings')

application = get_wsgi_application()