from django.shortcuts import render

from apps.store.models import Produit

# Create your views here.

def homepage(request):  # Permet de rendre la page html
    produits = Produit.objects.filter(vedette=True) # Importation des produits vedette uniquement

    context = {
        'produits': produits # Garde un historique des données
    }

    return render(request, 'homepage.html', context)

def contact(request):
    return render(request, 'contact.html')

def apropos(request):
    return render(request, 'apropos.html')