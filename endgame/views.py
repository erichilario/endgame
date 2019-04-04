from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import TemplateView
from whoisalive.models import Hero, Power

class IndexView(generic.ListView):
	context_object_name = 'hero_list'
	template_name = 'landingpage.html'

	def get_queryset(self):
		return Hero.objects.all()

class DataModelView(TemplateView):
	template_name = 'data-model.html'

	def get_context_data(self, **kwargs):
		context = super(DataModelView, self).get_context_data(**kwargs)
		context['hero_list'] = Hero.objects.all()
		return context

def handler404(request): #not sure how to pass "hero_list" to 404.html
    return render(request, '404.html', status=404)
def handler500(request):
    return render(request, '404.html', status=500)