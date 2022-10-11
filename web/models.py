from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify
# Create your models here.

class Blog(models.Model):
    image = VersatileImageField('Image',upload_to='images/blog/')
    heading = models.TextField()
    date = models.DateField(auto_now_add=True,editable=False)
    content = models.TextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural =("Blog")

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/gallery/')

    class Meta:
        verbose_name_plural =("Gallery")

    def __str__(self):
        return self.title


class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=255)
    is_active  = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Service Categories")

    def __str__(self):
        return str(self.category_name)


class Service(models.Model):
    service_name = models.CharField(max_length=255)
    image_1 = VersatileImageField('Image',upload_to='images/service/')
    image_2 = VersatileImageField('Image',upload_to='images/service/')
    image_3 = VersatileImageField('Image',upload_to='images/service/')
    details = models.CharField(max_length=1200)
    category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name_plural =("Service")


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =("Contact")


class Testimonial(models.Model):
    image = VersatileImageField('Image',upload_to='images/testimonial/')
    name = models.CharField(max_length=200)
    review = models.TextField()
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =("Testimonial")