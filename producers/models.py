from django.db import models

# Create your models here.

class Producer(models.Model):
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return f"Producer - {self.name}"