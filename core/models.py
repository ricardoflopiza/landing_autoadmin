# models.py
from django.db import models

class LandingPageSettings(models.Model):
    title = models.CharField(max_length=255, default='Welcome to our site')
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    background_color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code
    text_color = models.CharField(max_length=7, default='#000000')
    
    def __str__(self):
        return self.title