from django.shortcuts import render
from django.http import HttpResponse
from .models import SurveyQuestionAlternative, SurveyQuestion, Survey, SurveyUserAnswer
from .serializers import *


def test( request ):

    return HttpResponse('hallo world welcome to my page')


def index( request ) :

    return HttpResponse('imagine here a creative wonderful index test')


def SurveyView( request ):
    survey = Survey.objects.all()
    questions = SurveyQuestion.objects.all()
    alternatives = SurveyQuestionAlternative.objects.all()
    serializer = SurveySerializer( survey, many= True )
    print(serializer.data)

    return HttpResponse(serializer.data)


'''
class SurveyQuestionAlternativeView():
    pass


class SurveyQuestionView():
    pass



class SurveyUserAnswerView():
    pass
'''

