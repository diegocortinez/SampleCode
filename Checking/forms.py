from django import forms
from .models import Checking
from User.models import User


class NewChecking(forms.Form):
    user_id = forms.ModelChoiceField(queryset=User.objects.all())
    checking_balance = forms.IntegerField(label='Checking Balance')
    date_balance = forms.DateField(label='Date')
