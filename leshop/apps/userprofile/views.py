from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import FormulaireInscription

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        formulaireinscription = FormulaireInscription(request.POST)
     
        if formulaireinscription.is_valid():
            user = formulaireinscription.save()

            login(request, user)

            return redirect('homepage')

    else:
        formulaireinscription = FormulaireInscription()

    return render(request, 'inscription.html', {'formulaireinscription': formulaireinscription})

@login_required
def moncompte(request):
    user = request.user

    context = {
        'user' : user
    }
    return render(request, 'moncompte.html', context)
