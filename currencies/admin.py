from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'numeric_code', 'name', 'symbol', 'created_at', 'updated_at']
    list_filter = ['code', 'created_at', 'updated_at']
