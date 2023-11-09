from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem
from .forms import AddTodo


# Create your views here.
@login_required
def index(request):
    todos = TodoItem.objects.filter(user=request.user)
    form = AddTodo()
    if request.method == "POST":
        form = AddTodo(request.POST)
        if form.is_valid():
            todo_item = form.save(commit=False)
            todo_item.user = request.user
            todo_item.save()

            return redirect("index")
    return render(request, "todo/index.html", {"todos": todos, "form": form})


def delete(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == "POST":
        todo.delete()

    return redirect("index")


def update(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("index")
