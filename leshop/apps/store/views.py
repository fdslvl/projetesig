from django.shortcuts import render, get_object_or_404

from .models import Produit, Categorie

# Create your views here.

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
