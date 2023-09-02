from django.contrib import admin

from categories.models import Category, UserCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'type', 'is_deleted', 'created_at', 'updated_at']
    list_filter = ['parent', 'is_deleted', 'created_at', 'updated_at']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()


@admin.register(UserCategory)
class UserCategoryAdmin(CategoryAdmin):
    list_display = CategoryAdmin.list_display
    print(list_display)
