from django.shortcuts import render

from item.models import Catagory, Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold= False)
    catagories = Catagory.objects.all()
    
    return render(request,'core/index.html',{
        'catagories': catagories,
        'items':items,
    })


def contact(request):
    return render(request,'core/contact.html')


def signup(request):
    form = SignupForm
    
    return render(request,'core/signup.html',{
        'form': form
        
    })

