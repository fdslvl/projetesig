from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Produit, Categorie

# Create your views here.

def search(request):
    query = request.GET.get('query')
    produits = Produit.objects.filter(Q(nom__icontains=query) | Q(description__icontains=query))

    context = {
        'query': query,
        'produits': produits
    }

    return render(request, 'search.html', context)

def  produit_detail(request, categorie_slug, slug):
    produit = get_object_or_404(Produit, slug=slug) # Récupération du produit + id

    context = {
        'produit': produit
    }

    return render(request, 'produit_detail.html', context)

def categorie_detail(request, slug):
    categorie = get_object_or_404(Categorie, slug=slug) 
    produits = categorie.produits.all() #Ici je peux faire .produits car dans models.py il y a related_name

    context = {
        'categorie': categorie,
        'produits': produits
    }

    return render(request, 'categorie_detail.html', context)
