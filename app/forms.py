from django.contrib.auth.models import User
from django import forms
from .models import Inscription, Style,Subscriber

class InscriptionForm(forms.ModelForm):
    class Meta :
        model  = Inscription
        fields = ['name', 'last_name', 'first_name', 'style', 'birth_date', 'sexe','town_residence', 'number']

class StyleForm(forms.ModelForm):
    class Meta :
        model  = Style
        fields = ['name']

class NewsletterForm(forms.ModelForm):
    class Meta : 
        model = Subscriber
        fields = ['email']
        labels = {'email' : 'votre adresse e-mail'}
        widgets = { 
            'email' : forms.EmailInput(attrs = {'placeholder':'entrez votre email', 'class':'form-control'})
        }

class NewsletterEmailForm(forms.Form):
    subject = forms.CharField(max_length=300, label='Sujet')
    message = forms.CharField(widget=forms.Textarea, label='Message')