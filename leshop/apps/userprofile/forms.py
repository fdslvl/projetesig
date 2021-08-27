from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormulaireInscription(UserCreationForm):
    prenom = forms.CharField(max_length=50, required=True)
    nom = forms.CharField(max_length=50, required=True)
    email= forms.EmailField(max_length=255, required=True)

    def __init__(self, *args, **kwargs):
        super(FormulaireInscription, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input'
        self.fields['email'].widget.attrs['class'] = 'input'
        self.fields['password1'].widget.attrs['class'] = 'input'
        self.fields['password2'].widget.attrs['class'] = 'input'
        self.fields['prenom'].widget.attrs['class'] = 'input'
        self.fields['nom'].widget.attrs['class'] = 'input'

class Meta:
    model = User
    fields = ['username', 'pernom', 'nom', 'email', 'password1', 'password2']