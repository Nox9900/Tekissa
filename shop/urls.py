from django.urls import path 
from .views import CreateArticle , UpdateArticlesView, DeleteArticlesView ,voir_article
from . import url_name as  PathUrl 

app_name = "shop"

urlpatterns = [
     path('create-article/', CreateArticle.as_view(), name=PathUrl.CREATE_ARTICLE_VIEW_NAME),
     path('update-article/<int:pk>/', UpdateArticlesView.as_view(), name= PathUrl.UPDATE_ARTICLE_VIEW_NAME),
     path('delete-article/<int:pk>/', DeleteArticlesView.as_view(), name= PathUrl.DELETE_ARTICLE_VIEW_NAME),
     path('voir-article/<int:pk>/', voir_article, name= PathUrl.VOIR_ARTICLE_VIEW_NAME),
    
]
