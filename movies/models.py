from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True, null=True, 
        auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    rating_last_updated = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    rating_count = models.IntegerField(blank=True, null=True)
    rating_avg = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    score = models.FloatField(blank=True, null=True)
    idx = models.IntegerField(blank=True, null=True, help_text="Position IDs for ML")

