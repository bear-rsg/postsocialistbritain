from django.views.generic import (ListView, DetailView)
from . import models


class EventListView(ListView):
    """
    Event: List
    Class-based view to show the event list template
    """

    template_name = 'communities/event-list.html'
    queryset = models.Event.objects.filter(admin_published=True)


class EventDetailView(DetailView):
    """
    Event: Detail
    Class-based view to show the event detail template
    """
    template_name = 'communities/event-detail.html'
    queryset = models.Event.objects.filter(admin_published=True)
