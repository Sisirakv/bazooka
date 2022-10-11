
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import *
# Create your views here.


def index(request):
    gallery = Gallery.objects.all()[:5]
    service = Service.objects.all()[:8]
    testimonials = Testimonial.objects.all()
    context = {
        "is_home":True,
        'gallery' : gallery,
        "service" : service,
        "testimonials" : testimonials,
    }
    return render(request, 'index.html', context)


def about(request):
    service = Service.objects.all()[:8]
    context = {
        "is_about":True,
        "service":service
    }
    return render(request, 'about.html', context)
 

def service(request, id):
    category = ServiceCategory.objects.filter(is_active = True)
    service = Service.objects.get(id=id)
    context = {
        "is_service" : True,
        "category" : category,
        "service" : service,
    }
    return render(request, 'service-details.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        "is_gallery":True,
        'gallery' : gallery,
    }
    return render(request, 'gallery.html', context)


def blog(request):
    blog = Blog.objects.all()
    context = {
        "is_blog" : True,
        "blog" : blog,
    }
    return render(request, 'blog.html', context)


def blog_details(request, id):
    blog = Blog.objects.get(id = id) 
    
    print(blog)
    context = {
        "is_blog" : True,
        "blog" : blog,   
    }
    return render(request, 'blog-details.html', context)


def contact(request):
    forms = ContactForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            print(forms)
            forms.save()
            messages.info(request, "Your message was submitted successfully")
            return redirect('Contact')
    context = {
        'forms' : forms,
        "is_contact" : True,
    }
    return render(request,'contact.html', context)
    