from django.conf import settings

from apps.store.models import Produit

class Panier(object):
    def __init__(self, request):
        self.session = request.session
        panier = self.session.get(settings.CART_SESSION_ID) # Récupération de la session

        if not panier: # Si la session n'existe pas
            panier = self.session[settings.CART_SESSION_ID] = {}

        self.panier = panier

    def __iter__(self):
        produit_ids = self.panier.keys()

        produit_clean_ids = []

        for p in produit_ids:
            produit_clean_ids.append(p)

            self.panier[str(p)] ['produit'] = Produit.objects.get(pk=p)

        for item in self.panier.values():
            item['prix_total'] = float(item['prix']) * int(item['quantite'])

            yield item

    def __len__(self):
        return sum(item['quantite'] for item in self.panier.values())

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

    def retirer(self, produit_id): # Suppression du produit du panier
        if produit_id in self.panier: 
            del self.panier[produit_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.panier # Mise à jour de la session
        self.session.modified = True # Le navigateur sait que la session est modifiée

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_length(self): # Récupère le nombre d'éléments dans le panier
        return sum(int(item['quantite']) for item in self.panier.values())

    def get_prix_total(self):
            return sum(float(item['prix_total']) for item in self)