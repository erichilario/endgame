from django.http import HttpResponse, HttpResponseRedirect
#2md from django.http import Http404
#3rd from django.template import loader #not needed after importing render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView
from whoisalive.models import Hero, Power

class IndexView(generic.ListView): #display a list of objects
	context_object_name = 'hero_list'
	template_name = 'landingpage.html'
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

#def data_model_view(request):
#	return render(request, 'datamodel.html')

#def index(request):
#	
#	return render(request, 'landingpage.html')

class DataModelView(TemplateView):
	template_name = 'data-model.html'

#	def get_queryset(self):
#		return Hero.objects.all()
	def get_context_data(self, **kwargs):
		context = super(DataModelView, self).get_context_data(**kwargs)
		context['hero_list'] = Hero.objects.all()
		return context

		