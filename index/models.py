from django.db import models

# Create your models here.


class Commentaires (models.Model):
    name = models.CharField(blank=False, max_length=100)
    commentaire = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name