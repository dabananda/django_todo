from django.shortcuts import render, redirect
from todos.forms import TodoModelForm
from django.contrib import messages
from todos.models import Todo


def all_todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "home.html", context)


def add_todo(request):
    todo_form = TodoModelForm()
    if request.method == 'POST':
        todo_form = TodoModelForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect("all-todos")

    context = {
        'todo_form': todo_form
    }
    return render(request, "add_todo.html", context)


def update(request, id):
    todo = Todo.objects.get(id=id)
    todo_form = TodoModelForm(instance=todo)
    if request.method == "POST":
        todo_form = TodoModelForm(request.POST, instance=todo)
        if todo_form.is_valid():
            todo_form.save()
            return redirect("all-todos")

    context = {
        'todo_form': todo_form
    }
    return render(request, "add_todo.html", context)


def delete(request, id):
    if request.method == "POST":
        todo = Todo.objects.get(id=id)
        todo.delete()
        return redirect("all-todos")
