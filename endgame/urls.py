from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from .views import DataModelView

app_name = "whoisalive"
handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('whoisalive/', include('whoisalive.urls')),
    path('', views.IndexView.as_view(), name='index'),
    url(r'^data-model/', DataModelView.as_view(), name='data-model')
]
