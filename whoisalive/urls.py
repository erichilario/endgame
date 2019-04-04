from django.urls import path
from django.conf.urls import url
from . import views
from .views import DetailView

app_name = 'whoisalive'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]