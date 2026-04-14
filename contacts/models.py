from django.db import models

# Create your models here.

class MessageFromCustomer(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        #return f'Message from {self.name} ({self.email})'
        #return self.name
        return f'{self.name} - {self.subject}'
    
    class Meta:
        
        verbose_name = 'Сообщение от клиента' #'Message from Customer'
        verbose_name_plural = 'Сообщения от клиентов' #'Messages from Customers'
        ordering = ('-created_at',)

class Subscriber(models.Model):
    
    email = models.EmailField(unique=True)  #только уникальные email адреса могут быть добавлены в базу данных
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        
        verbose_name = 'Подписчик' #'Subscriber'
        verbose_name_plural = 'Подписчики' #'Subscribers'
        #ordering = ('-created_at',)

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
    