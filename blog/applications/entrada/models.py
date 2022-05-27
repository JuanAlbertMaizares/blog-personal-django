from django.db import models
from datetime import timedelta, datetime
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
from .managers import EntryManager

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
    objects = EntryManager()
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
    #
    slug = models.SlugField(editable=False, max_length=300)
    
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        """Unicode representation of Category."""
        return self.title
    
    def save(self, *args, **kwargs):
        #calculamos el total de segundo contenidos en la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        self.slug = slugify(slug_unique)
        
        super(Entry, self).save(*args, **kwargs)