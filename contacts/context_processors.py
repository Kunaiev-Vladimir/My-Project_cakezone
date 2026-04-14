from .models import Contacts
from .forms import SubscriberForm



def contacts(request):
    
    return {
        'subscriber_form': SubscriberForm(),
        'index_contacts': Contacts.objects.first()
    }