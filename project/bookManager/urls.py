from django.urls import include, path
from bookManager.views import HomeView, AuthorDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authors/<slug:slug>/', AuthorDetailView.as_view(), name='author-detail'),
]