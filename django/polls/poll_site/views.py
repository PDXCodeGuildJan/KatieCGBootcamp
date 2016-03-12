from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse

from .models import Question, Choice

# Create your views here.

def hello_world(request):
	# view controllers must always take at least a HttpResponse

	# Always need to return a HttpResponse
	return HttpResponse("<h1 style='color:purple'>Hello, World!</h1>")


def hello_world_render(request):

	questions = Question.objects.all()
	

	context = {
		"questions": questions,
		"name": "Katie",
		"last_name": "Dover",
		"shows": [
			"The Walking Dead",
			"Once Upon a Time",
			"Doctor Who"
		]
	}

	# Return a HttpResponse object, using the render function
	return render(request, "poll_site/index.html", context)

def corgi_page(request):
	return render(request, "poll_site/corgis.html")


def question_details(request, question_id):
	print("Passed Question", question_id)

	question = get_object_or_404(Question, pk=question_id)

	context = {
		'question': question, 
	}

	return render(request, 'poll_site/question_details.html', context)








