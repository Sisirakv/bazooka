
from . import views
from django.urls import path



urlpatterns = [
    
    path('',views.index, name="index"),
    path('About us/',views.about, name="About us"),
    path('Service/',views.service, name="Service"),
    path('Service Detatils/<int:id>/',views.service_detail, name="Service Detatils"),
    path('Gallery/',views.gallery, name="Gallery"),
    path('Blog/',views.blog, name="Blog"),
    path('Blog Details/<int:id>/',views.blog_details, name="Blog Details"),
    path('Contact/',views.contact, name='Contact'),
    
]