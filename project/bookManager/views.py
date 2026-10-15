from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from bookManager.models import Book, Author


class HomeView(View):
    def get(self, request):
        books = [
            {"title": "titulo 1", "cover": None, "authors": [{"name": "author 1"}]}]

        # books = None
        return render(request, template_name="base.html", context={"books": books})

class AuthorDetailView(View):
    def get(self, request):
        return HttpResponse("Authors detail page")