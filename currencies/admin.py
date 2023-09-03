from django.contrib import admin

from budget.admin_base import BaseAdmin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(BaseAdmin):
    list_display = ['code', 'numeric_code', 'name', 'symbol',
                    'is_deleted',
                    'created_at', 'updated_at']

    list_filter = ['code',
                   'is_deleted',
                   'created_at', 'updated_at']
