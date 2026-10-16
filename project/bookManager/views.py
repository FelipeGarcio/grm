from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from bookManager.models import Book, Author
from bookManager.forms import BookForm, AuthorForm\
from django.shortcuts import get_object_or_404


class HomeView(View):
    """ Class based view for the main/root page of the project.
    only has GET method with a mock book list.
    """
    def get(self, request):
        books = [{"title": "titulo 1", "cover": None, "authors": [{"name": "author 2"}]},
                 {"title": "titulo 2", "cover": None, "authors": [{"name": "author 4"}]},
                 {"title": "titulo 3", "cover": None, "authors": [{"name": "author 6"}]},
                 {"title": "titulo 4", "cover": None, "authors": [{"name": "author 8"}]},
                 {"title": "titulo 51", "cover": None, "authors": [{"name": "author 0o"}]},
                 {"title": "titulo 6", "cover": None, "authors": [{"name": "author a"}]}]
        # books = None
        return render(request, template_name="base.html", context={"books": None})


class AuthorDetailView(View):
    def get(self, request, slug):
        return HttpResponse("Authors detail page")


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, book_id=book_id)
        return render(request, template_name="book_page.html", context={"book": book})


class AddBookView(View):
    """Class based view with GET and POST methods, `GET` renders the template
    and POST receive and validate the book data.
    """
    def get(self, request):
        form = BookForm()
        return render(request, template_name="add_book_page.html", context={"form": form})

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        return render(request, template_name="add_book_page.html")