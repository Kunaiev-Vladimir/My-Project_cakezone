from django.db import models

# Create your models here.

class Contacts(models.Model):
    
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='contacts_photos')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    