from django.db import models
from User.models import User


class Savings(models.Model):
    savings_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
    savings_balance = models.BigIntegerField(blank=False)
    date_balance = models.DateField(blank=False)

