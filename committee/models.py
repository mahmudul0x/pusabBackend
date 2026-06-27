from django.db import models


class EcMember(models.Model):
    """An Executive Committee member for a given session year."""

    name = models.CharField(max_length=150)
    role = models.CharField(max_length=120)  # designation / podobi
    university = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField()  # session
    is_current = models.BooleanField(default=False)
    photo_url = models.URLField(max_length=600, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-year", "name"]

    def __str__(self):
        return f"{self.name} — {self.role} ({self.year})"
