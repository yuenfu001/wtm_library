from django.urls import path
from .views import display_books, delete_book, update_book

app_name="books_app"
urlpatterns =[
    path("display-books/",display_books,name="display_books"),
    path("delete-book/<str:book_id>/",delete_book,name="delete_book"),
    path("update-book/<str:book_request>/",update_book,name="update_book"),
]