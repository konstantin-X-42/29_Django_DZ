from django.urls import path
from blog.views import (
    BlogEntryListView,
    BlogEntryDetailView,
    BlogEntryCreateView,
    BlogEntryUpdateView,
    BlogEntryDeleteView,
)
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogEntryListView.as_view(), name='list'),
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogEntryDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BlogEntryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogEntryDeleteView.as_view(), name='delete'),
]
