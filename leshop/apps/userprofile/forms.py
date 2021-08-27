from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormulaireInscription(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

        labels = {'username' : 'Pseudo', 'first_name' : 'Prénom','last_name': 'Nom','email': 'Email', 'password1': 'Mot de passe', 'password2': 'Confirmation du mot de passe'}