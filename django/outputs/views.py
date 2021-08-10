from django.views.generic import (ListView, DetailView)
from . import models


class OutputListView(ListView):
    """
    Output: List
    Class-based view to show the output list template
    """

    template_name = 'outputs/output-list.html'
    queryset = models.Output.objects.filter(admin_published=True)


class OutputDetailView(DetailView):
    """
    Output: Detail
    Class-based view to show the output detail template
    """
    template_name = 'outputs/output-detail.html'
    queryset = models.Output.objects.filter(admin_published=True)
