from django.contrib import admin

from budget.admin_base import BaseAdmin
from .models import Currency, ExchangeRateCurrent, ExchangeRateHistory


@admin.register(Currency)
class CurrencyAdmin(BaseAdmin):
    list_display = ['code', 'numeric_code', 'name', 'symbol',
                    'is_deleted',
                    'created_at', 'updated_at']

    list_filter = ['code',
                   'is_deleted',
                   'created_at', 'updated_at']


@admin.register(ExchangeRateCurrent)
class ExchangeRateCurrentAdmin(BaseAdmin):
    list_display = ['currency1', 'currency2', 'rate_buy', 'rate_sell']


@admin.register(ExchangeRateHistory)
class ExchangeRateCurrentAdmin(BaseAdmin):
    list_display = ['currency1', 'currency2', 'rate_buy', 'rate_sell']
