from django.conf import settings

class Panier(object):
    def __init__(self, request):
        self.session = request.session
        panier = self.session.get(settings.SESSION_COOKIE_AGE) # Récupération de la session

        if not panier: # Si la session n'existe pas
            panier = self.session[settings.CART_SESSION_ID] = {}

        self.panier = panier

    def ajouter(self, produit, quantite =1, update_quantite=False): # Ajout de produit
        produit_id = str(produit.id)
        prix = produit.prix

        if produit_id not in self.panier: # Si l'id produit n'est pas dans le panier en crée une instance
            self.panier[produit_id] = {'quantite' : 0, 'prix' : prix, 'id': produit_id}

        if update_quantite: # S'il faut mettre à jour ou ajouter
            self.panier[produit_id] ['quantite'] = quantite # Mise à jour
        else:
            self.panier[produit_id] ['quantite'] = self.panier[produit_id] ['quantite'] + 1 # Ajout avec incrémentation de 1

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.panier # Mise à jour de la session
        self.session.modified = True # Le navigateur sait que la session est modifiée