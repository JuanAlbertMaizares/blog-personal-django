from django.db import models
from django.conf import settings
# Create your models here.
from model_utils.models import TimeStampedModel
from applications.entrada.models import Entry

class Favorites(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_favorites', on_delete= models.CASCADE)
    entry = models.ForeignKey(Entry, related_name='entry_favoritos', on_delete=models.CASCADE)
    
    class Meta: 
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada favorita'
        verbose_name_plural = 'Entreda favrita'
        
    def __str__(self):
        return self.entry_title