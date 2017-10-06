import os, random, string

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_iot_django.settings")

os.environ.setdefault("SECRET_KEY", ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16)))

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()