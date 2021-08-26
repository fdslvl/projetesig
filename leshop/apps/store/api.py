import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from apps.panier.panier import Panier

from apps.commande.utils import payer

from .models import Produit

from apps.commande.models import Commande, CommandeItem



def api_payer(request):
    panier = Panier(request)
    data = json.loads(request.body)
    jsonresponse = {'success' : True}
    prenom = data['prenom']
    nom = data['nom']
    email = data['email']
    adresse = data['adresse']
    npa = data['npa']
    localite = data['localite']

    commandeid = payer(request, prenom, nom , email, adresse, npa , localite)

    paye = True

    if paye == True:
        commande = Commande.objects.get(pk=commandeid)
        commande.paye = True
        commande.montant_paye = panier.get_prix_total()
        commande.save()

        panier.clear()

    return JsonResponse(jsonresponse)

def api_ajouter_au_panier(request):
    data = json.loads(request.body)
    jsonresponse = {'success' : True}
    produit_id = data['produit_id'] # Récupération de l'id produit
    update = data['update'] # Savoir si c'est mis à jour
    quantite = data['quantite']

    panier = Panier(request)

    produit = get_object_or_404(Produit, pk=produit_id)

    if not update: 
        panier.ajouter(produit=produit, quantite=1, update_quantite=False)
    else:
         panier.ajouter(produit=produit, quantite=quantite, update_quantite=True)

    return JsonResponse(jsonresponse)


def api_retirer_du_panier(request):
    data = json.loads(request.body)
    jsonresponse = {'success' : True}
    produit_id = str(data['produit_id']) # Récupération de l'id produit

    panier = Panier(request)
    panier.retirer(produit_id)

    return JsonResponse(jsonresponse)