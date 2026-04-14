
from django import forms
from .models import MessageFromCustomer, Subscriber



class MessageFromCustomerForm(forms.ModelForm):
    
    class Meta:
        model = MessageFromCustomer
        #fields = ['name', 'email', 'subject', 'message']
        fields = ('name', 'email', 'subject', 'message')


class SubscriberForm(forms.ModelForm):
    
    class Meta:
        model = Subscriber
        #fields = ['email']
        fields = ('email',)