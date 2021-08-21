from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self): #Dans la partie admin, montre directement le nom des catégories
        return self.nom

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='produits', on_delete=models.CASCADE) #Pour pouvoir avoir tous les produits d'une categorie, et que lorsque je supprime cette dernière tous les produits soient effacés
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True,  null=True)
    prix = models.FloatField()

    def __str__(self): 
        return self.nom