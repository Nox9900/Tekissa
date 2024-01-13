from django.shortcuts import render, redirect
from shop.models import Article, Categories, Image
from shop.data import ArticleInTemplate
from django.db.models import Q
from django.contrib import messages
from .forms import CommentForm
from .models import Commentaires



# Create your views here.

def homepage(request, *args, **kwargs):
    model = "homepage.html"

    #Partie concernant les categories et les articles de la Homepage
    #selection de toutes les categories dans la base de données
    
    all_categorie = Categories.objects.all()

    #Recuperation de 8 Articles publiés 
    articles = []
    articles_queryset = Article.objects.all()[:12]
    for article in articles_queryset:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))
    
    #Partie concernant des commentaires de la homepage
    
    #Selection des commentaires pour les afficher
    comment = Commentaires.objects.all()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre avis a été envoyé avec succes')
            return redirect ('index')
    else:
        form = CommentForm

    #Result
    return render(request, model, context={
        "categorie": all_categorie,
        'article_home': articles,
        'form':form,
        'comment': comment
    })


def voir_client_page (request, pk, *args, **kwargs):
   
    #La fbv qui s'occupe d'afficher les images correspondant à chaque article.
    #Elle s'applique sur button 'voir' des articles de la Homepage

    object = Article.objects.get(pk=pk)
    img = Image.objects.all().filter(article=object)
    template = 'voir-article-client.html'
    return render(request, template, context={
        'article': object,
        'img':img
    })

    
def recherche (request, *args, **kwargs):

    #la fbv qui s'occupe de la barre de recherche 

    articles = []
    if request.method == "GET":
        nom = request.GET.get('recherche')
        if nom == "":
            nom = "None"

        produit = Article.objects.filter(Q(article_name__icontains=nom) | Q(city__icontains=nom))
        count = produit.count()
        
        for article in produit:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

       

    return render(request, 'search.html', context={
        'recherche': articles, 
        'nom':nom,
        'count':count
    })

#partie "comment ca marche"

def guide(request):
    template = 'guide.html'
    return render(request, template)

def all_articles (request):
    template = 'articles.html'

    articles = []
    
    produits = Article.objects.all()
    produits_count = produits.count()

    for article in produits :
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            )) 

    return render (request, template, context={'produits':articles, 'count':produits_count})


#Partie concernant les categories
# Chaque fbv s'occupe d'afficher le contenu de chaque categorie (just-copy-and-paste for upcoming categories)

def electronique_categorie (request, *args, **kwargs):
    template = 'electronique_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()

    vehicule = Article.objects.filter(category=1)
    vehicule_annonces = vehicule.count()
    
    electronique = Article.objects.filter(Q(category=2))
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()
    
    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()

    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()


    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in electronique:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "categorie": articles, 
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })


def vehicule_categorie (request, *args, **kwargs):
    template = 'vehicule_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()
    

    vehicule = Article.objects.filter(Q(category=1))
    vehicule_annonces = vehicule.count()

    electronique= Article.objects.filter(category=2)
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()

    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()
    
    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()

    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in vehicule:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "articles": articles, 
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })

def immobilier_categorie (request, *args, **kwargs):
    template = 'immobilier_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()


    vehicule = Article.objects.filter(Q(category=1))
    vehicule_annonces = vehicule.count()

    electronique= Article.objects.filter(category=2)
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()
    
    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()

    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()


    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in immobilier:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "categorie": articles,
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })

def vetement_categorie (request, *args, **kwargs):
    template = 'vetement_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()

    vehicule = Article.objects.filter(Q(category=1))
    vehicule_annonces = vehicule.count()

    electronique= Article.objects.filter(category=2)
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()

    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()
    
    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()


    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in vetement:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "categorie": articles, 
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })

# Accessoire category

def accessoire_categorie (request, *args, **kwargs):
    template = 'accessoire_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()

    vehicule = Article.objects.filter(Q(category=1))
    vehicule_annonces = vehicule.count()

    electronique= Article.objects.filter(category=2)
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()

    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()
   
    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()

    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in accessoire:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "categorie": articles, 
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })

#categorie animaux
def animaux_categorie (request, *args, **kwargs):
    template = 'animaux_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()

    vehicule = Article.objects.filter(Q(category=1))
    vehicule_annonces = vehicule.count()

    electronique= Article.objects.filter(category=2)
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()

    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()
    
    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()


    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in animaux:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "categorie": articles, 
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })
#Autre categorie

def autre_categorie (request, *args, **kwargs):
    template = 'autres_categorie.html'
    articles = []

    #representation des categories dans la base de données
    # categorie 1 == Véhicule
    # categorie 2 == Electronique
    # categorie 3 == Immobilier
    # categorie 4 == Vetement
    # categorie 5 == accessoire
    # categorie 6 == animaux
    # categorie 7 == autre 

    first_categorie = Categories.objects.all()

    vehicule = Article.objects.filter(Q(category=1))
    vehicule_annonces = vehicule.count()

    electronique= Article.objects.filter(category=2)
    electronique_annonces = electronique.count()

    immobilier = Article.objects.filter(category=3)
    immobilier_annonces = immobilier.count()

    vetement = Article.objects.filter(category=4)
    vetement_annonces = vetement.count()
    
    accessoire = Article.objects.filter(category=5)
    accessoire_annonces = accessoire.count()

    animaux = Article.objects.filter(category=6)
    animaux_annonces = animaux.count()


    autre = Article.objects.filter(category=7)
    autre_annonces = autre.count()


    for article in autre:
            image_firt = Image.objects.filter(article_id=article.pk).first()
            image_article_count = Image.objects.filter(
                article_id=article.pk).count()
            articles.append(ArticleInTemplate(
                name=article.article_name,
                pk=article.pk,
                price=article.article_price,
                description=article.description,
                is_send=article.is_send,
                category=article.category,
                image=image_firt.thumbnail.url,
                city=article.city,
                user=article.user,
                image_article_count=image_article_count
            ))

    return render(request, template, context={
        "categorie": articles, 
        "first_categorie": first_categorie,
        'immobilier_annonce': immobilier_annonces,
        'electronique_annonce': electronique_annonces,
        'vetement_annonce': vetement_annonces,
        'animaux_annonce': animaux_annonces,
        'autre_annonce': autre_annonces,
        'accessoire_annonce': accessoire_annonces,
        'vehicule_annonce': vehicule_annonces,
    })
