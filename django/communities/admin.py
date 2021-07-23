from django.contrib import admin
from . import models

admin.site.site_header = 'CLiC Calendar: Admin Dashboard'


def approve_response(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to approved
    """
    queryset.update(admin_approved=True)


approve_response.short_description = "Approve selected responses (will appear on main site)"


def disapprove_response(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not approved
    """
    queryset.update(admin_approved=False)


disapprove_response.short_description = "Disapprove selected responses (will not appear on main site)"


class ResponseAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Responses in the Django admin
    """
    list_display = ('__str__',
                    'story',
                    'name',
                    'admin_approved',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('story', 'admin_approved')
    search_fields = ('response_text', 'name')
    list_per_page = 30
    ordering = ('-id',)
    actions = (approve_response, disapprove_response)


def publish_story(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(admin_published=True)


publish_story.short_description = "Publish selected stories (will appear on main site)"


def unpublish_story(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(admin_published=False)


unpublish_story.short_description = "Unpublish selected stories (will not appear on main site)"


class StoryAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Stories in the Django admin
    """
    list_display = ('story_text',
                    'story_image',
                    'year',
                    'month',
                    'admin_published',
                    'meta_created_datetime',
                    'meta_lastupdated_datetime')
    list_filter = ('year', 'month', 'admin_published')
    list_per_page = 30
    ordering = ('-id',)
    actions = (publish_story, unpublish_story)


# Register
admin.site.register(models.Response, ResponseAdminView)
admin.site.register(models.Story, StoryAdminView)
