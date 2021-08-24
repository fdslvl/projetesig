from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image


# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordre = models.IntegerField(default=0) #Permettre de trier par ordre numérique les catégories

    class Meta:
        ordering= ('ordre',)

    def __str__(self): #Dans la partie admin, montre directement le nom des catégories
        return self.nom

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='produits', on_delete=models.CASCADE) #Pour pouvoir avoir tous les produits d'une categorie, et que lorsque je supprime cette dernière tous les produits soient effacés
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255) # Slug = terme pour désigner le string en fin d'un URL qui permet l'identification
    description = models.TextField(blank=True,  null=True)
    prix = models.FloatField()
    vedette = models.BooleanField(default=False) # Attribut qui permet de définir quel produit est vedette et sera placé en homepage
    date_added = models.DateTimeField(auto_now_add=True) #Trie le produit par date lorsqu'il est ajouté
  
    image = models.ImageField(upload_to='media/uploads/',blank=True, null = True)
    thumbnail = models.ImageField(upload_to='media/uploads/',blank=True, null=True)

    class Meta:
        ordering = ('-date_added',) # Ici le '-' nous sert à trier de la date la plus récente

    def __str__(self): 
        return self.nom

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)): # Converti l'image choisie et en fait un template avec la taille donée, ici 300 par 200
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality =85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail