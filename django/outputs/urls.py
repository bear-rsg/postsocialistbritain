from django.urls import path
from . import views

app_name = 'outputs'

urlpatterns = [
    path('', views.OutputListView.as_view(), name='output-list'),
    path('<int:pk>/', views.OutputDetailView.as_view(), name='output-detail'),
]
