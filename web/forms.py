from logging import PlaceHolder

from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= '__all__'
        widgets= {
            'name': TextInput(attrs={'class':'form-control','name':'name','placeholder':'Enter your Name','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'form-control','name':'email','placeholder':'Enter your Email','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'form-control','name':'phone','placeholder':'Enter your phone number','required':'required','autocomplete':'off',}),
            'subject': TextInput(attrs={'class':'form-control','name':'subject','placeholder':'Enter Subject','required':'required','autocomplete':'off',}),
            'message':Textarea(attrs={'class':'form-control','name':'message','placeholder':'Your message','required':'required','autocomplete':'off',})
        }