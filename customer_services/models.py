

from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Installation', 'Meter Installation'),
        #
    )

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/')
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    resolution = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Service Request #{self.id}: {self.type} ({self.status})"
