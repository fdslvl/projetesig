from django.shortcuts import render

# Create your views here.

def panier(request):
    return render(request, 'panier.html')