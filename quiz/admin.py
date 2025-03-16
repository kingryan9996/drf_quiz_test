from django.contrib import admin
from .models import Quiz

# Register your models here.

#TODO: 8. admin페이지에서 Quiz 모델을 관리할 수 있도록 register(등록)
admin.site.register(Quiz)
# 등록하고 터미널 : python manage.py makemigrations
# Quiz모델에 대한 마이그레이션이 생성됨.
# 터미널 : python manage.py migrate
# Quiz모델에 대한 마이그레이션을 적용함.

#TODO: 9. admin페이지에서 Quiz 모델을 관리할 수 있도록 관리자(superuser)를 register(등록)
# 터미널 : python manage.py createsuperuser

#TODO: 10. Heroku에 배포하기
# 1. 터미널 : pip install django-cors-headers gunicorn psycopg2-binary whitenoise dj-database-url
# django-cors-headers : CORS(Cross-Origin Resource Sharing)를 설정할 수 있게 해주는 라이브러리
# gunicorn : WSGI 서버로 배포할 때 사용하는 라이브러리
# psycopg2-binary : PostgreSQL을 사용할 때 필요한 라이브러리
# whitenoise : 정적 파일의 사용을 돕는 미들웨어
# dj-database-url : 데이터베이스 URL을 파싱하는 라이브러리, psycopg2-binary마찬가지의 역할

#TODO: 11. requirements.txt 파일 생성
# 터미널 : pip freeze > requirements.txt
# 패키지 의존성에 관련 텍스트 파일을 생성