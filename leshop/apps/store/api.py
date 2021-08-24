from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from panier.panier import Panier

from .models import Produit

def api_ajouter_au_panier(request):
    jsonresponse = {'success' : True}
    produit_id = request.POST.get('produit_id') # Récupération de l'id produit
    update = request.POST.get('update') # Savoir si c'est mis à jour
    quantite = request.POST.get('quantitie', 1)

    panier = Panier(request)

    produit = get_object_or_404(Produit, pk=produit_id)

    if not update: # Si non mis à jour ajouter, sinon 
        panier.ajouter(produit=produit, quantite=1, update_quantite=False)
    else:
         panier.ajouter(produit=produit, quantite=quantite, update_quantite=True)

    return JsonResponse(jsonresponse)

