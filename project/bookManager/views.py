from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def home(request):
#     return render(request, template_name="base.html")

class HomeView(View):
    def get(self, request):
        books = [
            {"title": "title_1","description": "one description"},
            {"title": "title_2","description": "Two description"},
        ]
        return render(request, template_name="base.html", context={"books": books})