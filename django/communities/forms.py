from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3


class ResponseCreateForm(forms.ModelForm):
    """
    Form to specify fields in the Response create form
    """

    response_text = forms.CharField(max_length=1000,
                                    widget=forms.Textarea(),
                                    label='Your response')
    response_image = forms.ImageField(label='Upload image',
                                      help_text='Optional',
                                      required=False)
    author_name = forms.CharField(label='Name',
                                  widget=forms.TextInput(),
                                  help_text='Optional. Your name will be shown publicly alongside your response.',
                                  required=False)
    author_email = forms.EmailField(label='Email',
                                    widget=forms.TextInput(),
                                    help_text='Optional. Your email address will not be made publicly visible.',
                                    required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Response
        fields = ('response_text', 'response_image', 'author_name', 'author_email', 'story')


class StoryCreateForm(forms.ModelForm):
    """
    Form to specify fields in the Story create form
    """

    story_theme = forms.CharField(max_length=1000,
                                  help_text='Optional',
                                  label='Theme',
                                  required=False)
    story_text = forms.CharField(max_length=1000,
                                 widget=forms.Textarea(),
                                 label='Story text')
    story_image = forms.ImageField(label='Upload image',
                                   help_text='Optional',
                                   required=False)
    author_name = forms.CharField(label='Name',
                                  widget=forms.TextInput(),
                                  help_text='Optional. Your name will be shown publicly alongside your story.',
                                  required=False)
    author_email = forms.EmailField(label='Email',
                                    widget=forms.TextInput(),
                                    help_text='Optional. Your email address will not be made publicly visible.',
                                    required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Story
        fields = ('story_name', 'story_theme', 'story_text', 'story_image', 'author_name', 'author_email')
