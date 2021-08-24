from django.db import models

from apps.store.models import Produit

# Create your models here.

class Commande(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adresse= models.CharField(max_length=100)
    npa = models.CharField(max_length=100)
    localite = models.CharField(max_length=100)

    cree_le = models.DateTimeField(auto_now_add=True)

    paye = models.BooleanField(default=False)
    montant_paye = models.FloatField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.prenom

class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='items', on_delete=models.DO_NOTHING)
    prix = models.FloatField()
    quantite = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id