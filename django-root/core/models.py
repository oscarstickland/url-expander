from django.core.exceptions import ValidationError
from django.db import models

class URLExpansion(models.Model):
    slug = models.CharField(max_length=255, unique=True)
    url = models.URLField()

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

