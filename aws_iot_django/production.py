import os, random, string

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_iot_django.settings")

os.environ.setdefault("SECRET_KEY", ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16)))

application = get_wsgi_application()