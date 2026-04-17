from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacts
from .forms import MessageFromCustomerForm, SubscriberForm

# Create your views here.

def index(request):
    #1return HttpResponse("Contacts Index Page")
    #2return render(request, 'contacts.html')
    
    if request.method == 'POST':
        form = MessageFromCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            #можно добавить сообщение об успешной отправке формы, например, через messages framework
            return redirect('home:index')  # перенаправляем на home страницу после успешной отправки формы
        
        
    context = {
        'message_form': MessageFromCustomerForm(),
        'contacts': Contacts.objects.first()
    }
    return render(request, 'contacts.html', context = context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save() 
    return redirect('/')