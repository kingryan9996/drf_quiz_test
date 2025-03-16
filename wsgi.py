import os
from django.core.wsgi import get_wsgi_application

# DJANGO_SETTINGS_MODULE 환경 변수 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapi.settings')

application = get_wsgi_application()
