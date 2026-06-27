from rest_framework import viewsets

from config.permissions import IsAdminOrReadOnly

from .models import EcMember
from .serializers import EcMemberSerializer


class EcMemberViewSet(viewsets.ModelViewSet):
    queryset = EcMember.objects.all()
    serializer_class = EcMemberSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        year = self.request.query_params.get("year")
        if year:
            qs = qs.filter(year=year)
        if self.request.query_params.get("current") == "true":
            qs = qs.filter(is_current=True)
        return qs
