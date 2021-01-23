from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    return render(request, "indexc.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("test 3 page")
