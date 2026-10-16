from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from bookManager.models import Book, Author


class HomeView(View):
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
    def get(self, request):
        return HttpResponse("Authors detail page")


class BookDetailView(View):
    def get(self, request):
        return render(request, template_name="book_page.html")


class AddBookView(View):
    def get(self, request):
        return render(request, template_name="add_book_page.html")

    def post(self, request):
        return render(request, template_name="add_book_page.html")