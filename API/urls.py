from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('names', views.getNames),
    path('country/<str:name>/', views.getCountry)
]