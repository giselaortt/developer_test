from django.db import models


class Survey( models.Model ):
	#NUMBER_OF_QUESTIONS = 10
	LENGTH_SURVEY_NAME = 100
	survey_name = models.CharField(max_length=LENGTH_SURVEY_NAME)
	survey_id = models.IntegerField()
    def __str__(self):

        pass


class SurveyQuestion( models.Model ):
	LENGTH_QUESTION = 140
	question_text = models.CharField(max_length=LENGTH_QUESTION)
    survey = models.ManyToManyField( Survey )

    def __str__(self):

        return self.question_text


class SurveyQuestionAlternative( models.Model ):
	LENGTH_ALTERNATIVE = 100
	#question_id = models.IntegerField()
	alternative_text = models.CharField(max_length=LENGTH_ALTERNATIVE)	
    question = models.ForeingKey( SurveyQuestion )

    def __str__(self):

        return self.alternative_text


class SurveyUserAnswer( models.Model ):
    MAX_NAME_LENGTH = 50
    user_name = models.CharField( MAX_NAME_LENGTH )
    user_cpf = models.CharField( 11 )
    survey = models.ForeingKey( Survey )
    answers =  models.ForeignKey(SurveyQuestionAlternative) 
	#survey_id = models.IntegerField()

    def __str__(self):

        pass


