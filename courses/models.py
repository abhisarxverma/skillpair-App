from django.db import models
from users.models import User
from producers.models import Producer

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, null=False, related_name="all_courses")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.producer.name}"
    
    def serialize(self):
        return {
            "title" : self.title,
            "description" : self.description,
            "producer" : self.producer.name,
            "created_at" : self.created_at.strftime("%d/%m/%Y")
        }

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "course")

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
