from django import forms
from .models import User


class NewUser(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    middle_name = forms.CharField(label='Middle Name', required=False, max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    street_address = forms.CharField(label='Street Address', max_length=200)
    city = forms.CharField(label='City', max_length=50)
    state = forms.CharField(label='State', max_length=50)
    zip = forms.IntegerField(label='Zip')
    country = forms.CharField(label='Country', max_length=50)
    phone_number = forms.IntegerField(label='Phone Number')

