from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

def homepage(request):
    return render(request, "indexc.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("test 3 page")

def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books":books})

def add_book(request):
    form = request.POST
    book = Book(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=form["genre"],
        author=form["author"],
        year=form["year"][:10],
    )
    book.save()
    return redirect(books)

def delete_books(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(books)

def mark_books(request,id):
    book = Book.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(books)

def unmark_books(request,id):
    book = Book.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(books)   

def books_detail(request,id):
    books_detail_object = Book.objects.get(id=id)
    return render(request, "books_detail.html", {"books_detail_object":books_detail_object})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def unmark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect (test)

