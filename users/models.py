from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.

EXPERIENCE_CHOICES = [
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced")
    ]

class User(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )
    current_partner = models.ForeignKey("self", on_delete=models.SET_NULL, related_name="partner_users", null=True)


LANGUAGE_CHOICES = [
    ("python", "Python"),
    ("java", "Java"),
    ("c++", "C++"),
    ("javascript", "JavaScript"),
    ("ruby", "Ruby"),
    ("go", "Go"),
    ("swift", "Swift"),
    ("kotlin", "Kotlin"),
    ("rust", "Rust"),
    ("typescript", "TypeScript"),
    ("php", "PHP"),
    ("c#", "C#"),
    ("r", "R"),
    ("dart", "Dart"),
    ("shell", "Shell Scripting"),
]

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=100, default=f"Smart_Coder_{random.randint(1, 100)}")
    skills = models.TextField(default="Problem-solving, logical thinking, and adaptability")
    goals = models.TextField(default="To continuously improve and build impactful software solutions.")
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default="beginner")

class UserProgrammingLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="languages")
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    proficiency_level = models.IntegerField(default=1) 

    class Meta:
        unique_together = ("user", "language")

    def __str__(self):
        return f"{self.user.username} - {self.language} (Level {self.proficiency_level})"
