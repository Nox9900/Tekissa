from django.contrib import admin

from shop.models import Article, Categories, Image

# Register your models here.
@admin.register(Image)
class ImageArticleAdmin(admin.ModelAdmin):
  pass 

admin.site.register(Article)
admin.site.register(Categories)