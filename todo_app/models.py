from django.db import models


# Create your models here.
class ToDo_Task(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    deadline=models.DateField(blank=True)
    STATUS_CHOICES = [
        ('not_started', 'Not started'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
        ('postponed', 'Postponed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    def __str__(self):
        return self.title
