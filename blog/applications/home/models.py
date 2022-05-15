
from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Home( TimeStampedModel):
    """Model definition for Home."""

    # TODO: Define fields here
    title = models.CharField('Nombre', max_length=30)
    description = models.TextField()
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contact_email = models.EmailField('email de contacto', blank=True, null=True)
    phone = models.CharField('telefono de contacto', max_length=20)
    
    class Meta:
        """Meta definition for Home."""

        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        """Unicode representation of Home."""
        return self.title
class Suscribers(TimeStampedModel):
    """Model definition for Suscribers."""

    # TODO: Define fields here
    email = models.EmailField()
    class Meta:
        """Meta definition for Suscribers."""

        verbose_name = 'Suscribers'
        verbose_name_plural = 'Suscriberss'

    def __str__(self):
        """Unicode representation of Suscribers."""
        return self.email
class Contact(TimeStampedModel):
    """Model definition for Contact."""

    # TODO: Define fields here
    full_name = models.CharField('Nombres', max_length=60)
    email = models.EmailField()
    messagge = models.TextField()
    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.full_name 

