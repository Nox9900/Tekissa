from django.conf import settings
from django.db import models
from django.contrib.auth.models import  AbstractUser 
# Create your models here.

class User(AbstractUser):
  pass
  def __str__(self):
      return self.username
  


class Profile(models.Model):

  
  MALE  = "M"
  FEMALE = "F"
  
  SEXE_CHOICES  = (
    (MALE, 'Masculin'),
    (FEMALE, 'Feminin')
    ,
  )
  
  sex = models.CharField(max_length=15, choices=SEXE_CHOICES, default=MALE , verbose_name='genre')
  user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
  biography = models.TextField(blank=True, null=True , max_length=500)
  address = models.CharField(max_length=100, blank=True,null=True)
  cellphone  = models.CharField(max_length=100, blank=True, null=True)
  date_active = models.DateTimeField(auto_now_add=True)
  picture  = models.ImageField(blank=True, null=True, upload_to='UsersPicture')
  
  
  def first_name(self):
    return self.user.first_name 
  
  def last_name(self):
    return self.user.last_name 

  def __str__(self):
    return self.user.__str__()