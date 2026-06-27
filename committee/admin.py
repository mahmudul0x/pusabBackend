from django.contrib import admin

from .models import EcMember


@admin.register(EcMember)
class EcMemberAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "year", "is_current"]
    list_filter = ["year", "is_current"]
    search_fields = ["name", "role", "university"]
