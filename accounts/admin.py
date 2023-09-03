from django.contrib import admin

from budget.admin_base import BaseAdmin
from .models import AccountType, Account, CreditCard


@admin.register(AccountType)
class AccountTypeAdmin(BaseAdmin):
    list_display = ['name', 'description', 'is_deleted', 'created_at', 'updated_at']
    list_filter = ['name', 'is_deleted', 'created_at', 'updated_at']


@admin.register(Account)
class AccountAdmin(BaseAdmin):
    list_display = ['name', 'currency', 'balance', 'type', 'open_date',
                    'valid_till',
                    'credit_card',
                    'is_deleted',
                    'created_at', 'updated_at']
    list_filter = ['currency', 'type', 'open_date',
                   'valid_till',
                   'is_deleted',
                   'created_at', 'updated_at']


@admin.register(CreditCard)
class CreditCardAdmin(BaseAdmin):
    list_display = ['account', 'limit', 'due_date',
                    'is_deleted',
                    'created_at', 'updated_at']
    list_filter = ['account', 'limit', 'due_date',
                   'is_deleted',
                   'created_at', 'updated_at']
