from django.shortcuts import *
from django.contrib.auth.forms import *
from django.contrib.auth.models import *
from django.db import *
from django.contrib.auth import *
from .forms import *
from django.utils import timezone
from .models import *
from django.contrib.auth.decorators import *
from authentication.forms import *
def credits(request):
    return render(request, 'todo/credits.html')
def home(request):
        return render(request, 'todo/home.html', {'title':"My Work - The free todo web app"})
@login_required
def createtodo(request):
    if request.method=='GET':
        return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'title':"Create a todo"})
    else:
        try:
            form=TodoForm(request.POST)
            new_todo=form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error':'Bad Input', 'title':"Create a todo"})
@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'todo/currenttodos.html', {'form':UserCreationForm(), 'error': "Passwords didn't match. ", 'todos': todos, 'title':'Current todos'})
@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method=='GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/detailtodo.html', {'todo': todo, 'form':form})
    else:
        try:
            form=TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/currenttodos.html', {'form':TodoForm(), 'error':'Bad Input', 'todo':todo, 'title':todo.title})
@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.completed = timezone.now()
        todo.save()
        return redirect('currenttodos')
@login_required
def uncompletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.completed = None
        todo.save()
        return redirect('currenttodos')
@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')
@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, completed__isnull=False).order_by('-completed')
    return render(request, 'todo/completedtodos.html', {'form':UserCreationForm(), 'error': "Passwords didnt match.", 'todos': todos, 'title':'Completed todos'})
