from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [

    # Story
    path('', views.StoryListView.as_view(), name='story-list'),
    path('<int:pk>/', views.StoryDetailView.as_view(), name='story-detail'),

    # Response
    path('response/', views.ResponseCreateView.as_view(), name='response-create'),
    path('success/', views.ResponseCreateSuccessTemplateView.as_view(), name='response-create-success'),

]
