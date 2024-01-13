from . import url_name as  Path_Url
from django.urls import path
from .views import voir_client_page, recherche, guide, electronique_categorie, vehicule_categorie, immobilier_categorie, vetement_categorie, accessoire_categorie, animaux_categorie, autre_categorie, all_articles


urlpatterns = [
    path('client-article/<int:pk>', voir_client_page, name="client-article"),
    path('recherche/',recherche, name="recherche"),
    path('articles/',all_articles, name="all_articles"),
    path('guide/',guide, name="guide"),
    path('categories/electronique/', electronique_categorie, name="categorie_electronique"),
    path('categories/vehicule/', vehicule_categorie, name="categorie_vehicule"),
    path('categories/immobilier/', immobilier_categorie, name="categorie_immobilier"),
    path('categories/vetement/', vetement_categorie, name="categorie_vetement"),
    path('categories/accessoire/', accessoire_categorie, name="categorie_accessoire"),
    path('categories/animaux/', animaux_categorie, name="categorie_animaux"),
    path('categories/autres/', autre_categorie, name="categorie_autres"),
]
