from .panier import Panier

def panier(request):
    return {'panier': Panier(request)}