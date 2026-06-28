from rest_framework import serializers

from .models import EcMember


class EcMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcMember
        fields = [
            "id",
            "name",
            "role",
            "university",
            "year",
            "is_current",
            "is_convening",
            "photo_url",
        ]
        read_only_fields = ["id"]
