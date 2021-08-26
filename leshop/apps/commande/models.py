from django.db import models
from django.contrib.auth.models import User

from apps.store.models import Produit

# Create your models here.

class Commande(models.Model):
    EST_COMMANDE = 'commande'
    LIVRE = 'livre'
    ARRIVE = 'arrive'

    CHOIX_STATUT = (
        (EST_COMMANDE, 'Commandé'),
        (LIVRE, 'Livré'),
        (ARRIVE, 'Arrivé')
    )

    user = models.ForeignKey(User, related_name='commandes', on_delete=models.SET_NULL, blank=True, null=True)



    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adresse= models.CharField(max_length=100)
    npa = models.CharField(max_length=100)
    localite = models.CharField(max_length=100)

    cree_le = models.DateTimeField(auto_now_add=True)

    paye = models.BooleanField(default=False)
    montant_paye = models.FloatField(blank=True, null=True)

    date_livraison = models.DateTimeField(blank=True, null=True)
    statut = models.CharField(max_length=20, choices=CHOIX_STATUT, default=EST_COMMANDE)

    def __str__(self):
        return '%s' % self.prenom

    def get_total_quantite(self):
        return sum(int(item.quantite) for item in self.items.all())

class CommandeItem(models.Model):
    commande = models.ForeignKey(Commande, related_name='items', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, related_name='items', on_delete=models.DO_NOTHING)
    prix = models.FloatField()
    quantite = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id