from django.db import models
from courses.models import Course, Enrollment
from users.models import User

# Create your models here.

class Partner(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name="partner_match")
    partner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="partner")

    class Meta:
        unique_together = ("enrollment", "partner")

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("accepted", "Accepted"),
    ("rejected", "Rejected"),
]

class Request(models.Model):
    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default="pending"
    )

    def __str__(self):
        return f"Request({self.get_status_display()})"