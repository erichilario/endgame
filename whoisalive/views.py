from django.http import HttpResponse, HttpResponseRedirect
#2md from django.http import Http404
#3rd from django.template import loader #not needed after importing render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from whoisalive.models import Hero, Trivia

class IndexView(generic.ListView): #display a list of objects
	context_object_name = 'hero_list'
	template_name = 'whoisalive/index.html'
	#context_object_name = 'latest_question_list'

	def get_queryset(self):
		#1st """Return the last five published questions"""
		#1st return Question.objects.order_by('-pub_date')[:5]
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		#return Question.objects.filter(
		#	pub_date__lte=timezone.now()
		#).order_by('-pub_date')[:5] 
		# returns a queryset containing Questions whose pub_date
		# is less than or equal to -aka earlier than or equal to- timezone.now
		return Hero.objects.all()

class DetailView(generic.DetailView):
	model = Hero
	template_name = 'whoisalive/detail.html'