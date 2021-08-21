from django.db import models

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)