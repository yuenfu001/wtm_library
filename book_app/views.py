from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from .forms import CreateBookForm, UpdateBookForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def display_books(request):
    all_books = Book.objects.all()
    
    if request.method == "POST":
        book_form = CreateBookForm(request.POST)
        if book_form.is_valid():
            create_book =book_form.save(commit=False)
            create_book.save()
            book_form.save_m2m() # for saving genre which is a many to many field
            return redirect("books_app:display_books")

    else:
        book_form = CreateBookForm()
    context = {
        "display_books":all_books,
        "create_book":book_form
    }
    return render(request,"book/display_books.html",context)

@login_required
def update_book(request,book_request):
    # get_book = Book.object.get(id=book_request)
    get_book = get_object_or_404(Book,id=book_request)
    if request.method == "POST":
        update_book= UpdateBookForm(request.POST,instance=get_book)
        if update_book.is_valid():
            update_book.save()
            return redirect("books_app:display_books")
    else:
        update_book = UpdateBookForm(instance=get_book)
    context = {
        "update_book":update_book
    }
    return render(request,"book/update_book.html",context)

@login_required
def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("books_app:display_books")