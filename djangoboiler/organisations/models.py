from django.db import models
from djangoboiler.utils.models import BaseModel

# Create your models here.

class Organisation(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="organisations/logos", blank=True, null=True)

    def __str__(self):
        return self.name