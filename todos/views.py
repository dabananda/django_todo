from django.shortcuts import render, redirect
from todos.forms import TodoModelForm, CustomSignupForm
from django.contrib import messages
from todos.models import Todo
from django.contrib.auth import login, logout, authenticate


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


def signup(request):
    form = CustomSignupForm()

    if request.method == "POST":
        form = CustomSignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")

    context = {
        "form": form
    }

    return render(request, "signup.html", context)


def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")


def log_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")


def dashboard(request):
    return render(request, "dashboard.html")
