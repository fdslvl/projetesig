from django.shortcuts import render, get_object_or_404

from .models import Produit

# Create your views here.

def  produit_detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug) # Récupération du produit + id

    context = {
        'produit': produit
    }

    return render(request, 'produit_detail.html', context)