from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Savings.models import Savings


@admin.register(Savings)
class SavingsAdmin(ModelAdmin):
    pass
