from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^corgis$', corgi_page, name="corgis"),
]