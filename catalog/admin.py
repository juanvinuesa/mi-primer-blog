from django.contrib import admin
from .models import Author, Genero, Book, BookInstance,Sc_Article

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genero)
admin.site.register(BookInstance)
admin.site.register(Sc_Article)

# Register your models here.
