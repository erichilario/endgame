from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from whoisalive.models import Hero, Power

class IndexView(generic.ListView):
	context_object_name = 'hero_list'
	template_name = 'whoisalive/index.html'

	def get_queryset(self):
		return Hero.objects.all()

class DetailView(generic.DetailView):
	model = Hero
	
	template_name = 'whoisalive/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['hero_list'] = Hero.objects.all()
		context['power_list'] = Power.objects.order_by('id')
		# workaround for having the "Our Heroes" link to be of css class "active" from base.html
		context['isitactive'] = "active"
		return context