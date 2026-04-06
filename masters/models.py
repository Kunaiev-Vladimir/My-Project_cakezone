from django.db import models

# Create your models here.

class Staff(models.Model):
    
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff_photos')
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)