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
    #1 sort = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = 'Информация о нас' #'Home Info'
        verbose_name_plural = 'Информация о нас' #'Home Info'
        #1 ordering = ('sort',)
    
class Testimonial(models.Model):
    
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    #2 sort = models.PositiveSmallIntegerField()    
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = 'Отзыв' #'Testimonial'
        verbose_name_plural = 'Отзывы' #'Testimonials'
        #2 ordering = ('sort',)