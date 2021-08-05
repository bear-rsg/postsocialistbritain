from django.db import models
from datetime import date
from ckeditor.fields import RichTextField


class Event(models.Model):
    """
    A project-related event, e.g. a conference, seminar, etc.
    """

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    startdate = models.DateField()
    starttime = models.TimeField()
    finishdate = models.DateField()
    finishtime = models.TimeField()
    description = RichTextField(blank=True, null=True)
    bookingemail = models.CharField(max_length=255, blank=True, null=True)
    bookingurl = models.TextField(blank=True, null=True)
    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = RichTextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return str(self.story_text)[0:40]

    class Meta:
        verbose_name_plural = 'Stories'
        ordering = ['-meta_created_datetime', 'story_name', 'id']

    def __str__(self):
        return self.name

    @property
    def is_upcoming(self):
        return date.today() <= self.finishdate

    @property
    def is_past(self):
        return self.finishdate < date.today()
