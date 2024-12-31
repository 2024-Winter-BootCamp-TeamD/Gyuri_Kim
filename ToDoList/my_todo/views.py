from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    print("From DB:", todos)
    content = {'todos' : todos}
    return render(request,"my_todo/index.html", content)


def createTodo(request):
    user_input_str = request.POST['todoContent']

    new_todo = Todo(content = user_input_str)
    new_todo.save()

    #return HttpResponse("create todo를 하자! ==> " + user_input_str)
    return HttpResponseRedirect(reverse('index'))