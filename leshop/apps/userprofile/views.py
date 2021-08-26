from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import FormulaireInscription

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = FormulaireInscription(request.POST)
        
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('homepage')

    else:
        form = FormulaireInscription()

    return render(request, 'inscription.html', {'form': form})
