from django.urls import path
from . import views

urlpatterns = [
    path('', views.savings_home, name='savings_home'),
    path('new_savings/', views.new_savings, name='new_savings'),
    ]
