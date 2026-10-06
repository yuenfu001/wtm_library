from django.shortcuts import render
from author.models import Author
from book_app.models import Book
from genre_app.models import Genre
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_page(request):
    total_books = Book.objects.count()
    total_authors = Author.objects.count()
    total_genres = Genre.objects.count()
    liu ={
        "total_books":total_books,
        "total_authors":total_authors,
        "total_genres":total_genres,
    }
    return render(request,"base/index.html",liu)
