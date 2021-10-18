from django.contrib import admin
from . import models


def publish_output(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish_output.short_description = "Publish selected outputs (will appear on main site)"


def unpublish_output(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish_output.short_description = "Unpublish selected outputs (will not appear on main site)"


class OutputAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Responses in the Django admin
    """
    list_display = ('name',
                    'description',
                    'image',
                    'file',
                    'video',
                    'link',
                    'admin_published')
    list_filter = ('admin_published', )
    search_fields = ('name', 'description', 'file', 'link', 'video')
    list_per_page = 30
    ordering = ('name', '-id')
    actions = (publish_output, unpublish_output)


# Register
admin.site.register(models.Output, OutputAdminView)
