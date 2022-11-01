from django.db import models


class User(models.Model):
    ACTIVE = [('Y', 'Yes'),
              ('N', 'No')]

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=False)
    street_address = models.CharField(max_length=200, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    zip = models.IntegerField(blank=False)
    country = models.CharField(max_length=50, blank=False)
    phone_number = models.BigIntegerField(blank=False)
    active = models.CharField(max_length=3, choices=ACTIVE, default='Y')

