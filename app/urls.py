from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inscription', views.inscription, name='inscription'),
    path('inscription_delete/<int:inscription_id>/', views.inscription_delete, name='inscription_delete'),
    path('inscription_modif/<int:inscription_id>/', views.inscription_modif ,name='inscription_modif'),
    path('inscription_detail/<int:inscription_id>/', views.inscription_detail ,name='inscription_detail'),
    path('style', views.style, name='style'),
    path('style_modif/<int:style_id>/', views.style_modif, name='style_modif'),
    path('style_delete/<int:style_id>/', views.style_delete, name='style_delete'),
    path('Subscriber_newsletter', views.Subscriber_newsletter, name='Subscriber_newsletter'),
    path('admin_detail/', views.admin, name='admin'),
    path('inscription_search/', views.inscription_search, name='inscription_search'),
    path('subscribe_search/', views.subscribe_search, name='subscribe_search'),
    path('send_messages', views.send_messages, name='send_messages'),
    path('affiche/', views.affiche, name='affiche'),
    path('decouverte/', views.decouverte, name='decouverte'),
    path('equipe/', views.equipe, name='equipe'),
]