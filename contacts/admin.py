from django.contrib import admin
from .models import Contacts, MessageFromCustomer, Subscriber 

# Register your models here.

admin.site.register(Contacts)
admin.site.register(MessageFromCustomer)
admin.site.register(Subscriber)
