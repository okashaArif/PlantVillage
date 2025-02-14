from django.db import models
from django.contrib.auth.models import User

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self) -> str:
        return f'Message From {self.name}'
