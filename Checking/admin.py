from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Checking.models import Checking


@admin.register(Checking)
class CheckingAdmin(ModelAdmin):
    pass

