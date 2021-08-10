from django.db import models
from datetime import date
from ckeditor.fields import RichTextField


class Output(models.Model):
    """
    A project-related output, e.g. a PDF doc, image, or link.
    """

    name = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='outputs-images', blank=True, null=True)
    file = models.FileField(upload_to='outputs-files', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = RichTextField(blank=True, null=True)

    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-id']
