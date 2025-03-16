from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random

#TODO : 3. quiz/urls.py와 myapt/urls.py는 다른 파일
# quiz/urls.py : quiz.app에 대한 url을 관리
# myapi/urls.py : 전체 프로젝트에 대한 url을 관리
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizSerializer(randomQuizs, many=True)
    # many=True : 여러개의 데이터를 직렬화할 때 사용
    return Response(serializer.data)