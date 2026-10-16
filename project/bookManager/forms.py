from django.forms import ModelForm
from bookManager.models import Book, Author

class BookForm(ModelForm):
    """Django form for the `Book` Model
    """
    class Meta:
        model = Book
        fields = ["title", "cover", "author"]

class AuthorForm(ModelForm):
    """Django form for the `Author` model
    """
    class meta:
        model = Author 
        fields = ["name"]
