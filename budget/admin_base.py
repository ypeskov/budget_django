from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    def delete_selected(self, request, queryset):
        self.delete_queryset(request, queryset)

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            obj.delete()
