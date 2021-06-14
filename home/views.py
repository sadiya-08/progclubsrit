from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from home.models import Gallery

# Create your views here.
def index(request):
    fea=Gallery.objects.filter(flag="F")
    if request.method == "POST":
        contact=Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name=name
        contact.phone=phone
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.date=datetime.today()
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'index.html',{'fea':fea})

def compt(request): 
    return render(request, 'compt.html')

def resources(request):
    return render(request, 'resources.html')

def testimonals(request):
    return render(request, 'testimonals.html')

def blog(request):
    return render(request, 'blog.html')

