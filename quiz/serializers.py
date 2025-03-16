from rest_framework import serializers
from .models import Quiz

# TODO:2. QuizSerializer 클래스를 선언
# serializers : django 모델 데이터를 JSON 타입으로 바꿔주는(직렬화) 코드
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        # fields = ['title', 'body'] # title, body만 사용하겠다는 의미
        # Quiz 모델 데이터가 주어지면 title, body, answer를 JSON 타입으로 바꿔줌.
        fields = '__all__'# 모든 필드를 사용하겠다는 의미
