"""
WSGI config for aws_iot_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, random, string

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_iot_django.settings")
try:
	sec = os.environ['SECRET_KEY']
except:
	os.environ.setdefault("SECRET_KEY", ''.join(random.choice(string.letters + string.digits) for i in range(16)))

application = get_wsgi_application()
