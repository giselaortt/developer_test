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

    #Sera que survey precisa de serializer ? a ideia eh que haja apenas 1 survey, nao eh ?
    serializer = SurveySerializer( survey, many= True )
    alternative_serializer = AlternativeSerializer( alternatives, many = True )
    question_serializer = SurveyQuestionSerializer( questions, many = True )

    return HttpResponse(serializer.data + question_serializer.data
                    + alternative_serializer.data)


'''
class SurveyQuestionAlternativeView():
    pass



class SurveyQuestionView():
    pass



class SurveyUserAnswerView():
    pass
'''

