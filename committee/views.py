from rest_framework import viewsets

from config.permissions import IsAdminOrReadOnly

from .models import EcMember, LeaderMessage
from .serializers import EcMemberSerializer, LeaderMessageSerializer


class EcMemberViewSet(viewsets.ModelViewSet):
    queryset = EcMember.objects.all()
    serializer_class = EcMemberSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        year = self.request.query_params.get("year")
        if year:
            qs = qs.filter(year=year, is_convening=False)
        if self.request.query_params.get("current") == "true":
            qs = qs.filter(is_current=True)
        if self.request.query_params.get("convening") == "true":
            qs = qs.filter(is_convening=True)
        return qs


class LeaderMessageViewSet(viewsets.ModelViewSet):
    """President / General Secretary messages — looked up by role."""

    queryset = LeaderMessage.objects.all()
    serializer_class = LeaderMessageSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "role"
