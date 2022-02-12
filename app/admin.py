from typing import List
from django.contrib import admin
from .models import(
    Client,
    Maison,
    Ventes,
    Commandes,
)

@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    List_display = ['id', 'user', 'nom', 'prenom', 'adresse', 'ville', 'Num_tel', 'State']



@admin.register(Maison)
class MaisonModelAdmin(admin.ModelAdmin):
    List_display = ['id', 'title', 'Prix_de_vente', 'Prix_reduit', 'description', 'quartier', 'commune', 'image_maison']


@admin.register(Ventes)
class VentesModelAdmin(admin.ModelAdmin):
    List_display = ['id', 'user', 'Maison', 'prix']



@admin.register(Commandes)
class CommandesModelAdmin(admin.ModelAdmin):
    List_display = ['id', 'user', 'client', 'maison', 'prix', 'date_commande', 'Statut']
    