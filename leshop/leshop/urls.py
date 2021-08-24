"""leshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.panier.views import panier_detail
from apps.core.views import homepage, contact, apropos
from apps.store.views import produit_detail, categorie_detail

from apps.store.api import api_ajouter_au_panier, api_retirer_du_panier

urlpatterns = [
    path('', homepage, name='homepage'),
    path('panier/', panier_detail, name='panier'),
    path('contact/', contact, name='contact'),
    path('apropos/', apropos, name='apropos'),
    path('admin/', admin.site.urls),

    # API

    path('api/ajouter_au_panier/', api_ajouter_au_panier, name= 'api_ajouter_au_panier'),
    path('api/retirer_du_panier/', api_retirer_du_panier, name= 'api_retirer_du_panier'),


    # Store

    path('<slug:categorie_slug>/<slug:slug>/', produit_detail,  name='produit_detail'),
    path('<slug:slug>/', categorie_detail,  name='categorie_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
