from django.contrib import admin

from budget.admin_base import BaseAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ['user', 'is_deleted', 'date_of_birth']
    raw_id_fields = ['user']
    list_filter = ['user']
