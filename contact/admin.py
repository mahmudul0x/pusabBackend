from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "university", "session", "subject", "is_read", "created_at"]
    list_filter = ["is_read", "created_at", "university"]
    search_fields = ["name", "phone", "email", "university", "village", "school", "college", "message"]
