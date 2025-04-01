from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.username

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", blank=False, null=False)
    email = models.EmailField(verbose_name="Электронная почта", blank=False, null=False)
    text = models.TextField(max_length=500, verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Сообщение от {self.name}"