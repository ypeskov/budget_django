from django.contrib import admin

from more_admin_filters import MultiSelectDropdownFilter

from categories.models import Category, UserCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'type', 'is_deleted', 'created_at', 'updated_at']
    list_filter = [('parent__name', MultiSelectDropdownFilter), 'type', 'is_deleted', 'created_at', 'updated_at']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


@admin.register(UserCategory)
class UserCategoryAdmin(CategoryAdmin):
    list_display = CategoryAdmin.list_display + ['user']
    list_filter = CategoryAdmin.list_filter + [('user__username', MultiSelectDropdownFilter)]
