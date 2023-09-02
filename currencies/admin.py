from django.contrib import admin

from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'numeric_code', 'name', 'symbol',
                    'is_deleted',
                    'created_at', 'updated_at']

    list_filter = ['code',
                   'is_deleted',
                   'created_at', 'updated_at']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
