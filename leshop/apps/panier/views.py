from django.shortcuts import render

from .panier import Panier

# Create your views here.

def panier_detail(request):
    panier = Panier(request)

    context = {
        'panier' : panier
    }

    return render(request, 'panier.html', context)