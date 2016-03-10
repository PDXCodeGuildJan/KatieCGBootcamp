from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def hello_world(request):
	# view controllers must always take at least a HttpResponse

	# Always need to return a HttpResponse
	return HttpResponse("<h1 style='color:purple'>Hello, World!</h1>")


def hello_world_render(request):

	context = {
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