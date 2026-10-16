from django.forms import ModelForm
from bookManager.models import Book, Author

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "cover", "author"]

class AuthorForm(ModelForm):
    class meta:
        model = Author 
        fields = ["name"]
