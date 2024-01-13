
from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Categories(models.Model):

  DEFAULT_CHOICE = 'Autres'
  choix = (

    ('Véhicule', 'Véhicule'),
    ('Electronique','Electronique'),
    ('Immobilier', 'Immobilier'),
    ('Vetements', 'Vetements'),
    ('Accessoires', 'Accessoires'),
    ('Animaux', 'Animaux'),
    ('Autres', 'Autres')

  )
  name = models.CharField(max_length=255, choices=choix, default=DEFAULT_CHOICE)
  image = models.ImageField(upload_to="CategoryPhoto")

  def __str__(self) -> str:
    return self.name 


class Article(models.Model):

  article_name = models.CharField(max_length=15,blank=False, verbose_name='Nom')
  article_price = models.DecimalField(max_digits=9, decimal_places=0 , verbose_name='Prix')
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Utilisateur')
  slug = models.SlugField(null=True, blank=True)
  category = models.ForeignKey(Categories, on_delete=models.CASCADE, )
  description= models.TextField(blank=True, null=True)
  is_send = models.BooleanField(default=False, help_text="  ")
  city = models.CharField(max_length=50, blank=False, verbose_name="ville")
  
  def save(self , *args, **kwargs):
    self.slug = slugify(self.article_name)
    return super().save(*args, **kwargs)

  def __str__(self):
    return self.article_name 


class Image(models.Model):
  article= models.ForeignKey(Article, on_delete=models.CASCADE)
  thumbnail = models.ImageField(upload_to='ArticlePhoto', blank=False)
  
  def __str__(self):
    return self.thumbnail.name 
