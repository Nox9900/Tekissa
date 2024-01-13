from django.contrib import admin
from .models import Commentaires

# Register your models here.

@admin.register(Commentaires)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('name', 'commentaire', 'date')
    list_filter = ('date',)
    search_field = ('name', 'commentaire')
    actions = ['approuver_commentaire']


    def approuver_commentaire (self, request, queryset):
        queryset.update(active=True)