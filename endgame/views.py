from django.http import HttpResponse, HttpResponseRedirect
#2md from django.http import Http404
#3rd from django.template import loader #not needed after importing render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from whoisalive.models import Hero, Trivia

def index(request):
	return render(request, 'landingpage.html')