from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_book', views.create_book),
    path('books/<int:id>', views.books_desc),
    path('add_author/<int:id>', views.add_author),
    path('authors', views.authors),
    path('create_author', views.create_author),
    path('author/<int:id>', views.authors_desc),
    path('add_book/<int:id>', views.add_book)
]