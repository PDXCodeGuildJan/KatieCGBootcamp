from django.shortcuts import render
from django.http.response import HttpResponse

def hello_world(request):

	return HttpResponse("<h1 style='color: purple'>Hello, World!<h1>")

def hello_world_render(request):

	context = {
		"name": "Katie",
		"port_pieces": [
			"Zen Garden",
			"JavaPic"
		]
	}

	return render(request, "port_site/index.html", context)