from django.shortcuts import render

# Create your views here.

def panier_detail(request):
    return render(request, 'panier.html')