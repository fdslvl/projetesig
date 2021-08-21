from django.shortcuts import render

# Create your views here.

def homepage(request):  # Permet de rendre la page html
    return render(request, 'homepage.html')

def contact(request):
    return render(request, 'contact.html')
