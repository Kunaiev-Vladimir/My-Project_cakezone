from django.db import models

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    sort = models.PositiveSmallIntegerField()
    is_vsible = models.BooleanField(default=True)
    
class Dish(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='menu_photos')
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    sort = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 