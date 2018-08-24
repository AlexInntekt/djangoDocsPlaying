from django.urls import path, include
from . import views

from django.contrib import admin

from django.contrib.auth import views as auth_views


urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('dates', views.display_date, name='display_date'),
  path('display/<int:i>', views.displayInd, name='display'),

  path('login', auth_views.login, {'template_name': 'blog/login.html'}),

]



