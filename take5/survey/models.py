from django.db import models


class Survey( models.Model ):
	#NUMBER_OF_QUESTIONS = 10
	LENGTH_SURVEY_NAME = 100
	survey_name = models.CharField(max_length=LENGTH_SURVEY_NAME)
	survey_id = models.IntegerField()
	id_question_1 = models.IntegerField()
	id_question_2 = models.IntegerField()
	id_question_3 = models.IntegerField()
	id_question_4 = models.IntegerField()
	id_question_5 = models.IntegerField()
	id_question_6 = models.IntegerField()
	id_question_7 = models.IntegerField()
	id_question_8 = models.IntegerField()
	id_question_9 = models.IntegerField()
	id_question_10 = models.IntegerField()
    def __str__(self):


class SurveyQuestion( models.Model ):
	#NUMBER_OF_ALTERNATIVES = 5
	LENGTH_QUESTION = 140
	question_id = models.IntegerField()
	question_text = models.CharField(max_length=LENGTH_QUESTION)
	#o survey ao qual pertence essa pergunta
	survey_id = models.IntegerField()
	alternative_id_1 = models.IntegerField()
	alternative_id_2 = models.IntegerField()
	alternative_id_3 = models.IntegerField()
	alternative_id_4 = models.IntegerField()
	alternative_id_5 = models.IntegerField()

    def __str__(self):

        return self.question_text


class SurveyQuestionAlternative( models.Model ):
	LENGTH_ALTERNATIVE = 100
	question_id = models.IntegerField()
	alternative_text = models.CharField(max_length=LENGTH_ALTERNATIVE)	
	alternative_id = models.IntegerField()

    def __str__(self):

        return self.alternative_text


class SurveyUserAnswer( models.Model ):
    MAX_NAME_LENGTH = 50
    user_name = models.CharField( MAX_NAME_LENGTH )
	user_answer = models.IntegerField()
	survey_id = models.IntegerField()
	user_answer_question_1 = models.CharField( max_length = 1 )
	user_answer_question_2 = models.CharField( max_length = 1 )
	user_answer_question_3 = models.CharField( max_length = 1 )
	user_answer_question_4 = models.CharField( max_length = 1 )
	user_answer_question_5 = models.CharField( max_length = 1 )
	user_answer_question_6 = models.CharField( max_length = 1 )
	user_answer_question_7 = models.CharField( max_length = 1 )
	user_answer_question_8 = models.CharField( max_length = 1 )
	user_answer_question_9 = models.CharField( max_length = 1 )
	user_answer_question_10 = models.CharField( max_length = 1 )

    def __str__(self):
        pass
