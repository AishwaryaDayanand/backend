"""
WSGI config for diagnostic_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from diagnostic_django.asgi import APPLICATION

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diagnostic_django.settings')

application = get_wsgi_application()
