from django.contrib import admin

from more_admin_filters import MultiSelectDropdownFilter

from budget.admin_base import BaseAdmin
from .models import Operation


@admin.register(Operation)
class OperationAdmin(BaseAdmin):
    list_display = ['user', 'label', 'type', 'amount', 'source_account', 'op_date', 'currency',
                    'is_deleted',
                    'created_at', 'updated_at']
    list_filter = [('user__username', MultiSelectDropdownFilter),
                   'source_account', 'destination_account', 'type', 'category',
                   'is_deleted', 'created_at', 'updated_at']
