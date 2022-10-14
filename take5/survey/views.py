from django.shortcuts import render

from django.http import HttpResponse
from .models import SurveyQuestionAlternative, SurveyQuestion, Survey, SurveyUserAnswer


def test( request ):
    return HttpResponse('hallo world welcome to my page')


def index( request ) :
    return HttpResponse('imagine here a creative wonderful index test')


class SurveyQuestionAlternativeView(): 
    pass


class SurveyQuestionView(): 
    pass


class SurveyView(): 
    pass


class SurveyUserAnswerView(): 
    pass


