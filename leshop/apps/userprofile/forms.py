from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormulaireInscription(UserCreationForm):
    prenom = forms.CharField(max_length=50, required=True)
    nom = forms.CharField(max_length=50, required=True)
    email= forms.EmailField(max_length=255, required=True)

class Meta:
    model = User
    fields = ['username', 'pernom', 'nom', 'email', 'password1', 'password2']