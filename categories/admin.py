from django.contrib import admin

from more_admin_filters import MultiSelectDropdownFilter

from budget.admin_base import BaseAdmin
from categories.models import Category, UserCategory


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ['name', 'parent', 'type', 'is_deleted', 'created_at', 'updated_at']
    list_filter = [('parent__name', MultiSelectDropdownFilter), 'type', 'is_deleted', 'created_at', 'updated_at']


@admin.register(UserCategory)
class UserCategoryAdmin(BaseAdmin):
    list_display = CategoryAdmin.list_display + ['user']
    list_filter = CategoryAdmin.list_filter + [('user__username', MultiSelectDropdownFilter)]
