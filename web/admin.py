from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Contact)
admin.site.register(Blog) 
admin.site.register(Gallery)

admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Clinet)