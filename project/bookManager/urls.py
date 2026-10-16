from django.urls import include, path
from bookManager.views import HomeView, AuthorDetailView, BookDetailView, AddBookView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/', BookDetailView.as_view(), name="book_detail"),
    path('add-book', AddBookView.as_view(), name="add_book"),
    path('authors/<slug:slug>/', AuthorDetailView.as_view(), name='author-detail'),
]