from django.urls import path

#from .views import *
from . import views as LocalViews

urlpatterns = [
    path('', LocalViews.HomePageView.as_view(), name='home'),
    path('about', LocalViews.AboutPageView.as_view(), name='about'),
]