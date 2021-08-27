from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import FormulaireInscription, UserprofileForm

# Create your views here.

def inscription(request):
    if request.method == 'POST':
        formulaireinscription = FormulaireInscription(request.POST)
        userprofileform = UserprofileForm(request.POST)
        
        if formulaireinscription.is_valid() and userprofileform.is_valid():
            user = formulaireinscription.save()

            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            userprofile.save()

            login(request, user)

            return redirect('homepage')

    else:
        formulaireinscription = FormulaireInscription()
        userprofileform = UserprofileForm()

    return render(request, 'inscription.html', {'formulaireinscription': formulaireinscription, 'userprofileform': userprofileform})

@login_required
def moncompte(request):
    return render(request, 'moncompte.html')
