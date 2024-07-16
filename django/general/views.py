from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    """
    Class-based view to show the welcome template
    """
    template_name = 'general/welcome.html'


class AboutTemplateView(TemplateView):
    """
    Class-based view to show the about template
    """
    template_name = 'general/about.html'


class EngagementTemplateView(TemplateView):
    """
    Class-based view to show the engagement template
    """
    template_name = 'general/engagement.html'


class EducationTemplateView(TemplateView):
    """
    Class-based view to show the education template
    """
    template_name = 'general/education.html'


class CookiesTemplateView(TemplateView):
    """
    Class-based view to show the cookies template
    """
    template_name = 'general/cookies.html'
