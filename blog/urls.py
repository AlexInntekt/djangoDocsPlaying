from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('dates', views.display_date, name='display_date'),
  path('display/<int:i>', views.displayInd, name='display'),

]