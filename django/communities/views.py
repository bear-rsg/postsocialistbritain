from django.views.generic import (CreateView, TemplateView, ListView, DetailView)
from django.urls import reverse_lazy
from . import (models, forms)


class StoryListView(ListView):
    """
    Story: List
    Class-based view to show the story list template
    """

    template_name = 'communities/story-list.html'
    queryset = models.Story.objects.filter(admin_published=True)


class StoryDetailView(DetailView):
    """
    Story: Detail
    Class-based view to show the story detail template

    Note that this is a more complex DetailView than normal, as it also includes:
        - A form for submitting a new response to the current story
        - A list of responses related to the current story
    Therefore, suitable content needs to be added to this view's context, via the get_context_data() method
    """
    template_name = 'communities/story-detail.html'
    queryset = models.Story.objects.filter(admin_published=True)

    def get_context_data(self, **kwargs):
        # Get current context
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        # Add form for creating an response
        context['response_create_form'] = forms.ResponseCreateForm
        # Add list of responses that relate to the current story and have been approved by admin
        context['responses'] = models.Response.objects.filter(story=self.object.id, admin_approved=True)
        return context


class ResponseCreateView(CreateView):
    """
    Class-based view to create a new models.Response object in the database
    This works by passing data to the forms.ResponseCreateForm form

    Note that this view doesn't have a template
    It's only intended to receive post requests and redirect if successful

    The template that includes the HTML form for submitting to this view is in the above StoryDetailView.
    See the get_context_data() method in the StoryDetailView for more details.
    """

    form_class = forms.ResponseCreateForm
    success_url = reverse_lazy('communities:response-create-success')


class ResponseCreateSuccessTemplateView(TemplateView):
    """
    Class-based view to show the response create success template
    """

    template_name = 'communities/response-create-success.html'
