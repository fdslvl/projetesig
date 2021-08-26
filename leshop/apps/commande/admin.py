import datetime

from django.urls import reverse
from django.contrib import admin

from .models import Commande, CommandeItem

# Register your models here.

def nom_commande(obj):
    return '%s %s' % (obj.prenom, obj.nom)
nom_commande.short_description = 'Nom'

def admin_commande_livre(modeladmin, request, queryset): #Customisation option action
    for commande in queryset:
        commande.date_livraison = datetime.datetime.now()
        commande.statut = Commande.LIVRE
        commande.save()
    return
admin_commande_livre.short_description = 'Marqué comme livré'

class CommandeEnCours(admin.TabularInline): #Montre le produit commandé dans la commande
    model = CommandeItem
    raw_id_fields = ['produit']

class CommandeAdmin(admin.ModelAdmin): #Affiche un libéllé, un filtre , une barre de recherche et permet d'utiliser action
    list_display = ['id', nom_commande, 'statut', 'cree_le']
    list_filter= ['cree_le', 'statut']
    search_fields= ['prenom','adresse']
    inlines = [CommandeEnCours]
    actions = [admin_commande_livre]

admin.site.register(Commande, CommandeAdmin)
admin.site.register(CommandeItem)