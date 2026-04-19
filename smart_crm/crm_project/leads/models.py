from django.db import models

from .utils import calculate_score
# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('interested', 'Interested'),
        ('converted', 'Converted'),
        ('lost', 'Lost'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    source = models.CharField(max_length=50)  # Instagram, Website, etc.
    
    score = models.IntegerField(default=0)
    
    follow_up_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print("SAVE METHOD CALLED")
        self.score = calculate_score(self.status, self.source)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.name