from django.shortcuts import render

from .panier import Panier

# Create your views here.

def panier_detail(request):
    panier = Panier(request)
    produitstring = ' '

    for item in panier:
        produit = item['produit']
        url = '/%s/%s/' % (produit.categorie.slug, produit.slug)
        b = "{'id': '%s', 'nom': '%s', 'prix': '%s', 'quantite': '%s', 'prix_total' : '%s', 'thumbnail': '%s', 'url': '%s'}," % (produit.id, produit.nom, produit.prix, item['quantite'], item['prix_total'], produit.thumbnail.url, url)

        produitstring = produitstring + b

    context = {
        'panier' : panier,
        'produitstring' : produitstring
    }

    return render(request, 'panier.html', context)