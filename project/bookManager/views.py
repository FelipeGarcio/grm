from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def home(request):
#     return render(request, template_name="base.html")

class HomeView(View):
    def get(self, request):
        books = None
        return render(request, template_name="base.html", context={"books": books})