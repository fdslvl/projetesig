import datetime
import os

from random import randint

from apps.panier.panier import Panier

from apps.commande.models import Commande, CommandeItem

def payer(request, prenom, nom , email, adresse, npa , localite):
    commande = Commande(prenom = prenom, nom = nom, email = email, adresse = adresse, npa = npa, localite = localite)

    if request.user.is_authenticated:
        commande.user = request.user

    commande.save()

    panier = Panier(request)


    for item in panier:
        CommandeItem.objects.create(commande=commande, produit= item['produit'], prix = item['prix'], quantite = item['quantite'])

    return commande.id