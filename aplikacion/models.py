from django.db import models

# Create your models here.
class Service (models.Model):
    # emriVaribli = models.TipiFushen(parametra)
    service_icon = models.CharField(max_length=200, null=True, blank=True)
    service_title = models.CharField(max_length=200, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.service_title}"