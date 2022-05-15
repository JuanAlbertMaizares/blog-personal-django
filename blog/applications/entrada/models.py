from django.db import models
from django.conf import settings
# Create your models here.
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

class Category(TimeStampedModel):
    """Model definition for Category."""

    # TODO: Define fields here
    short_name = models.CharField('Nombre Corto', max_length=15, unique=True)
    name = models.CharField('nombre', max_length=30)
    
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
class Tag(TimeStampedModel):
    """Etiqueta descriptiva sobre la entrada."""

    # TODO: Define fields here
    name = models.CharField('nombre', max_length=30)
    
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name
    
class Entry(TimeStampedModel):
    """Model definition for Category."""

    # TODO: Define fields here
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField('Titulo', max_length=200)
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField('imagen', upload_to='Entry')
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)
    
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        """Unicode representation of Category."""
        return self.title