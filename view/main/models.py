from django.db import models

class VisitRecord(models.Model):
    date = models.DateField(primary_key=True)
    count = models.PositiveIntegerField(default=0)

