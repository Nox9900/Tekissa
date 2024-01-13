
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["user", 'is_send']
        widgets = {
            'article_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Nom de l'article"}),
            'category': forms.Select(attrs={'class': 'form-input', 'placeholder': "Categorie",}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 5  , 'placeholder': 'description'}),
            'article_price': forms.NumberInput(attrs={'class': 'form-input'  , 'placeholder': "Price de l'article "}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Ville - Exemple:'Pointe-noire'"})
        }


class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['user', 'slug']
        widgets = {
            'article_name': forms.TextInput(attrs={'class': 'form-input'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 5}),
            'article_price': forms.NumberInput(attrs={'class': 'form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-input', 'placeholder': "Ville"})

        }
