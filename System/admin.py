from django.contrib import admin

from django.contrib.auth import get_user_model
from .models import Patient, Physician, Appointment
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(Patient)
admin.site.register(Physician)
admin.site.register(Appointment)
