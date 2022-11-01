from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_user),
    path('add_user', views.add_user),

]
