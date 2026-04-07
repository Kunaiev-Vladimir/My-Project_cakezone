from django.db import models
# 1 from menu.models import Category

# Create your models here.

class Service(models.Model):
    
    # 1 menu_service = models.ForeignKey(Category, on_delete=models.CASCADE)
    menu_service = models.ForeignKey('menu.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services/')
    #2 sort = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = 'Сервис' #'Service'
        verbose_name_plural = 'Сервисы' #'Services'
        #2 ordering = ('sort',)