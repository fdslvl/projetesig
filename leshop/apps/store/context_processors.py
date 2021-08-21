from .models import Categorie

def menu_categories(request):
    categories = Categorie.objects.all() # Importation des catégories de la database

    return {'menu_categories': categories}