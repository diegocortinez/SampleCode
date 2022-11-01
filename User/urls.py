from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('new_user/', views.new_user, name='new_user'),
    path('deactivate_user/<int:id>', views.deactivate_user, name='deactivate_user'),
    ]
