from django.contrib import admin

from .models import AccountType, Account, CreditCard


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    list_filter = ['name', 'created_at', 'updated_at']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'currency', 'balance', 'type', 'open_date', 'valid_till',
                    'credit_card', 'created_at', 'updated_at']
    list_filter = ['currency', 'type', 'open_date', 'valid_till',
                   'credit_card', 'created_at', 'updated_at']


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ['account', 'limit', 'due_date', 'created_at', 'updated_at']
    list_filter = ['account', 'limit', 'due_date',  'created_at', 'updated_at']
