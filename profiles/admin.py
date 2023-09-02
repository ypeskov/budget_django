from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_deleted', 'date_of_birth']
    raw_id_fields = ['user']
    list_filter = ['user']

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()