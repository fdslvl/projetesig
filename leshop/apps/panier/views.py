from django.shortcuts import render

from .panier import Panier

# Create your views here.

def panier_detail(request):
    panier = Panier(request)
    produitstring = ' '

    for item in panier:
        produit = item['produit']
        b = "{'id': '%s', 'nom': '%s', 'prix': '%s', 'quantite': '%s', 'prix_total' : '%s'}," % (produit.id, produit.nom, produit.prix, item['quantite'], item['prix_total'])

        produitstring = produitstring + b

    context = {
        'panier' : panier,
        'produitstring' : produitstring
    }

    return render(request, 'panier.html', context)