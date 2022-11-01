from django import forms
from .models import Savings
from User.models import User


class NewSavings(forms.Form):
    user_id = forms.ModelChoiceField(queryset=User.objects.all())
    savings_balance = forms.IntegerField(label='Savings Balance')
    date_balance = forms.DateField(label='Date')
