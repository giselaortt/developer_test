from rest_framework import serializers
from survey.models import *


class AlternativeSerializer( serializers.ModelSerializer ):

    class Meta:
        model = SurveyQuestionAlternative
        fields = '__all__'


class SurveyQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = '__all__'


