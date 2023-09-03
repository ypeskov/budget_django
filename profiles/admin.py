from django.contrib import admin

from budget.admin_base import BaseAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ['user', 'base_currency', 'date_of_birth', 'is_deleted']
    raw_id_fields = ['user']
    list_filter = ['user', 'date_of_birth']
