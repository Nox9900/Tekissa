from django import forms
from .models import Commentaires

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaires
        exclude = ["date", "active"]
        widgets = {
            'name': forms.TextInput(attrs={'class':'name', 'placeholder':'Votre nom'}),
            'commentaire': forms.Textarea(attrs={'class':'comment',  'placeholder':'Votre commentaire'}),

        }
    