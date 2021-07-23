from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from ckeditor.fields import RichTextField
import logging

logger = logging.getLogger(__name__)


class Story(models.Model):
    """
    The story that a researcher poses to the users
    """

    story_name = models.CharField(max_length=255, unique=True)
    story_text = RichTextField()
    story_image = models.ImageField(upload_to='communities-stories-images', blank=True, null=True)
    # Admin fields
    admin_published = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return str(self.story_text)[0:40]

    class Meta:
        verbose_name_plural = 'Stories'
        ordering = ['-meta_created_datetime', 'story_name', 'id']


class Response(models.Model):
    """
    The response that a user submits in response to a story
    """

    response_text = models.TextField()
    response_image = models.ImageField(upload_to='communities-responses-images', blank=True, null=True)
    author_name = models.CharField(blank=True, max_length=255)
    author_email = models.EmailField(blank=True)
    # Foreign key fields
    story = models.ForeignKey(Story, related_name='responses', on_delete=models.PROTECT)
    # Admin fields
    admin_approved = models.BooleanField(default=False)
    admin_notes = models.TextField(blank=True, null=True)
    # Metadata fields
    meta_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    meta_lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __str__(self):
        return self.response_text if len(self.response_text) < 100 else (f'${self.response_text[:97]}...')

    def save(self, *args, **kwargs):
        """
        Email the research team when a new model is saved
        """

        # Check if this is a new response
        if self.meta_created_datetime is None:
            # Send email alert to research team
            try:
                send_mail('Post-Socialist Britain: New response',
                          'There has been a new response submitted to the Post-Socialist Britain website.',
                          settings.DEFAULT_FROM_EMAIL,
                          settings.NOTIFICATION_EMAIL,
                          fail_silently=False)
            except Exception:
                logger.exception("Failed to send email")

        # Save new object
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-meta_created_datetime']
