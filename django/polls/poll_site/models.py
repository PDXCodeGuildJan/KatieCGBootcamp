from django.db import models

# Create your models here.

class Question(models.Model):
	"""Defines the Question class and model."""
	# Establish global variables for the class Quesetion
	
	# Define the attributes of the Question Model
	# 	that are stored in the database

	# Create a text field with a limit of 200 characters
	question_text = models.CharField(max_length=200)
	# Create a time stamp labeled "Date Published"
	pub_date = models.DateTimeField("Date Published")

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	"""Defines the Choice class and Model."""
	# Create a text field for each choice to go with the question
	choice_text = models.CharField(max_length=150)
	# Create a basic incrementer to count each vote for each choice
	votes = models.PositiveSmallIntegerField(default=0)
	# Relationship between choice and question
	question_id = models.ForeignKey(Question)

	def __str__(self):
		return self.choice_text

