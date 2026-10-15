import uuid
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers/", blank=True)
    author = models.ManyToManyField("Author", related_name="books", blank=False)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.name