from django.urls import path, include
from .views import helloAPI, randomQuiz

#TODO : 4.quiz/urls.py는 quiz.app에 대한 url을 관리
# urlpatterns를 만들고
urlpatterns = [
    path('hello/', helloAPI),
    #TODO: 7. views/py에 추가한 'randomQuiz'API를
    # path("<int:id>/", randomQuiz)를 추가
    path("<int:id>/", randomQuiz),
]