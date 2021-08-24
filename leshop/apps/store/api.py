import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.panier.panier import Panier

from .models import Produit

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