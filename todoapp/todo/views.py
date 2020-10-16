from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todoitem


def todoview(request):
    all_todo_item = Todoitem.objects.all()
    context = {
        'all_todo_item': all_todo_item
    }
    return render(request, 'todo/todo.html', context)


def addtodo(request):
    new_item = Todoitem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')


def deleteTodo(request, todo_id):
    item_to_delete = Todoitem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')


