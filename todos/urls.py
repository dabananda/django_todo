from django.urls import path
from todos.views import *

urlpatterns = [
    path('', all_todos, name="all-todos"),
    path('add-todo/', add_todo, name="add-todo"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]
