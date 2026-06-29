from rest_framework import permissions, throttling, viewsets
from rest_framework.exceptions import ValidationError

from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactSubmitThrottle(throttling.AnonRateThrottle):
    """Max 3 submissions per hour per IP for the public contact/join form."""
    scope = "contact_submit"


class ContactMessageViewSet(viewsets.ModelViewSet):
    """Anyone may submit (POST). Only admins can read, update or delete."""

    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_throttles(self):
        if self.action == "create":
            return [ContactSubmitThrottle()]
        return []

    def perform_create(self, serializer):
        # Reject honeypot: if the hidden `website` field has any value, it's a bot.
        honeypot = self.request.data.get("website", "")
        if honeypot:
            raise ValidationError({"detail": "Invalid submission."})
        serializer.save()
