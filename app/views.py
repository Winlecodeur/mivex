from django.shortcuts import render, redirect, get_object_or_404 
from .models import Inscription, Style, Subscriber
from .forms import InscriptionForm, StyleForm, NewsletterForm, NewsletterEmailForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings 
from django.db.models import Q

#ici je defini le home, la partie d'accueil | here i created my home, it's easy don't much code 
def home(request):
    return render (request, 'index.html')

#ici je defini le form d'inscription  | here i created a way for an user subscribe in the app 
def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else : 
        form = InscriptionForm()
    return render (request, 'inscription.html',{'form':form})
#ici je developpe une manière de supprimer une inscription de la base de données | here i created a way to delete an inscription
def inscription_delete(request, inscription_id):
    if request.user.is_superuser:
        inscription = get_object_or_404(Inscription, id=inscription_id)
        inscription.delete()
        return redirect('admin')

#ici je developpe une manière de recherche une inscription | here i created a way to search an inscription 
def inscription_search(request):
    if request.user.is_superuser:
        query = request.GET.get('q')
        resultats = []
        if query : 
            resultats = Inscription.objects.filter(Q(name__icontains=query))
        return render (request, 'search.html',{'query':query, 'resultats':resultats})
    else : 
        return redirect('home')
def inscription_modif(request, inscription_id):
    if request.user.is_superuser : 
        inscription = Inscription.objects.get(id=inscription_id)
        if request.method == 'POST':
            form = InscriptionForm(request.POST, instance=inscription)
            if form.is_valid():
                form.save()
                return redirect ('admin')
        else : 
            form = InscriptionForm(instance=inscription)
        return render (request, 'inscription_modif.html', {'inscription':inscription, 'form':form})
    else : 
        return redirect('home')
def inscription_detail(request, inscription_id):
    if request.user.is_superuser : 
        inscription = Inscription.objects.get(id=inscription_id)
        return render (request, 'inscription_detail.html', {'inscription':inscription})
    else : 
        return redirect('home')
#ici je developpe le form pour mettre le nom du style | here i created a way to add a name style 
def style(request):
    if request.method == 'POST':
        form = StyleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('admin')
    else : 
        form = StyleForm()
    return render (request, 'style.html', {'form':form})
#ici je developpe une manière de modifier le nom du style | here i created a way to modifie a name style
def style_modif (request, style_id):
    if request.user.is_superuser : 
        style = Style.objects.get(id=style_id)
        if request.method == 'POST':
            form = StyleForm(request.POST, instance=style)
            if form.is_valid():
                form.save()
                return redirect ('admin')
        else : 
            form = StyleForm(instance=style)
        return render (request, 'style_modif.html', {'style':style, 'form':form})
    else : 
        return redirect('home')

#ici je developpe une manière de supprimer un style | here i created a way to delete a style
def style_delete(request, style_id):
    if request.user.is_superuser:
        style = get_object_or_404(Style, id=style_id)
        style.delete()
        return redirect('admin')
    else : 
        return redirect ('home')
#ici je developpe le panel admin, avec le style et autres en todo_lsit | here i created my admin profil with a todo_list 
def admin(request):
    if request.user.is_superuser : 
        style = Style.objects.all()
        inscription = Inscription.objects.all()
        subscribers = Subscriber.objects.all()
        return render (request, 'admin.html',{'style':style, 'inscription':inscription, 'subscribers':subscribers})
    else :
        return redirect ('home')

#ici je crée une newsletter pour que les abonnés s'y abonne | here i created my newsletter for help an user to subscribe in
def Subscriber_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'vous êtes maintenant abonné à notre newsletter!')
            return redirect('/#newsletter')
    else :
        form = NewsletterForm()
    return render (request, 'index.html', {'form':form})
def subscribe_search(request):
    if request.user.is_superuser:
        query = request.GET.get('q')
        resultats = []
        if query : 
            resultats = Subscriber.objects.filter(Q(email__icontains=query))
        return render (request, 'subscribe_search.html',{'query':query, 'resultats':resultats})
    else : 
        return redirect('home')

#ici je developpe une manière d'envoyer un message à tous les utlisateurs qui sont dans ma newsletter | here i created a way to send a message for our subscribers
def send_messages(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = NewsletterEmailForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                subscribers = Subscriber.objects.all()
                recipient_list = [subscriber.email for subscriber in subscribers]
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
                messages.success(request, 'la newsletter a été envoyée avec succès')
                return redirect ('admin')
        else : 
            form = NewsletterEmailForm()
        return render (request, 'admin.html',{'form':form})
    else : 
        return redirect('home')

#ici je developpe 3 detail different affiche, decouverte et equipe
def equipe(request):
    return render (request, 'equipe.html')
def affiche (request):
    return render (request, 'affiche.html')
def decouverte(request):
    return render (request, 'decouver.html')