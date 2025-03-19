from django.db import models

# Create your models here.

class Task(models.Model):
    status_choices=(
        ('pending','pending'),
        ('completed','completed'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
