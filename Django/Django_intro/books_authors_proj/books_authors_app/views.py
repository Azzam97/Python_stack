from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, "index.html", context)


def create_book(request):
    Book.objects.create(title = request.POST['title'],
                        desc = request.POST['desc']
                    )
    return redirect('/')


def books_desc(request,id):
    context = {
        'books': Book.objects.get(id = id),
        'authors': Author.objects.all()
    }
    return render(request, "books.html", context)


def add_author(request, id):
    book = Book.objects.get(id = id)
    author = Author.objects.get(id = int(request.POST['authors']))
    book.authors.add(author)
    return redirect(f"/books/{book.id}")


def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, "authors.html", context)


def create_author(request):
    Author.objects.create(first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        notes = request.POST['notes']
                    )
    return redirect('/authors')


def authors_desc(request, id):
    context = {
        'authors': Author.objects.get(id = id),
        'books': Book.objects.all()
    }
    return render(request, "author_desc.html", context)


def add_book(request, id):
    author = Author.objects.get(id = id)
    book = Book.objects.get(id = int(request.POST['books']))
    author.book.add(book)
    return redirect(f"/author/{author.id}")
