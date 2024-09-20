from django.db import models

# Create your models here.
class PageVisit(models.Model):
    page_visit = models.TextField(blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

class FieldTypes(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
