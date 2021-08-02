from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	movies = Movie.objects.all().order_by('-id')[:12]
	context = {
		'movies':movies
	}
	return render(request, '01-home.html', context)