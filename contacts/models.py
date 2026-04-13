from django.db import models

# Create your models here.

class Contacts(models.Model):
    
    address = models.TextField() #address = models.CharField(max_length=255) мой вариант был
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
    
    def __str__(self):
        return self.address
    
    class Meta:
        
        verbose_name = 'Контакт' #'Contact'
        verbose_name_plural = 'Контакты' #'Contacts'
        ordering = ('sort',)
    