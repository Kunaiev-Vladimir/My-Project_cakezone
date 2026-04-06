from django.db import models

# Create your models here.

class HomeInfo(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='home/')

    experience = models.IntegerField(default=10)
    cake_specialist = models.IntegerField(default=50)
    complete_project = models.IntegerField(default=200)
    happy_clients = models.IntegerField(default=500)
    
class Testimonial(models.Model):
    
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')    