"""
WSGI config for books project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')

application = get_wsgi_application()

# 以下を末尾に追記
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

