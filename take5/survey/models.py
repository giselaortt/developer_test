from django.db import models


class Survey( models.Model ):
    #NUMBER_OF_QUESTIONS = 10
    LENGTH_SURVEY_NAME = 100
    name = models.CharField(max_length=LENGTH_SURVEY_NAME)
    #survey_id = models.IntegerField()
    #Problem: how to print the questions if they are not assigned from here?
    #def __str__(self):
    #    return self.name


class SurveyQuestion( models.Model ):
    LENGTH_QUESTION = 140
    question_text = models.CharField(max_length=LENGTH_QUESTION)
    #many to many or foreignt key? eis a questao.
    #survey = models.ManyToManyField( Survey )
    survey = models.ForeingKey( Survey, on_delete = models.CASCADE )
    def __str__(self):
        return self.question_text


class SurveyQuestionAlternative( models.Model ):
    LENGTH_ALTERNATIVE = 100
    #question_id = models.IntegerField()
    text = models.CharField(max_length=LENGTH_ALTERNATIVE)  
    question = models.ForeingKey( SurveyQuestion, on_delete = models.CASCADE )
    def __str__(self):
        return self.alternative_text


class SurveyUserAnswer( models.Model ):
    MAX_NAME_LENGTH = 50
    user_name = models.CharField( MAX_NAME_LENGTH )
    user_cpf = models.CharField( 11 )
    survey = models.ForeingKey( Survey )
    answers =  models.ForeingKey( SurveyQuestionAlternative, on_delete = models.CASCADE ) 
    #survey_id = models.IntegerField()
    #def __str__(self):
    #    return self.user_name
