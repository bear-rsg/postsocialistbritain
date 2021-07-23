from django import forms
from . import models
from captcha.fields import ReCaptchaField, ReCaptchaV3


class ResponseCreateForm(forms.ModelForm):
    """
    Form to specify fields in the answer create form
    """

    response_text = forms.CharField(max_length=1000,
                                    widget=forms.Textarea(attrs={'placeholder': 'Respond to this story here'}),
                                    label='Response')
    response_image = forms.ImageField(label='Optional. Provide an image to illustrate your response.')
    author_name = forms.CharField(label='Name',
                                  widget=forms.TextInput(attrs={'placeholder': '(Optional)'}))
    author_email = forms.EmailField(label='Email',
                                    widget=forms.TextInput(attrs={
                                        'placeholder':
                                        '(Optional. Your email address will not be made publicly visible.)'
                                    }))
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = models.Response
        fields = ('response_text', 'response_image', 'author_name', 'author_email', 'story')
