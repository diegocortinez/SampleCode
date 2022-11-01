from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking_home, name='checking_home'),
    path('new_checking/', views.new_checking, name='new_checking'),

    ]
