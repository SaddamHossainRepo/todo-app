
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoview, name='view'),
    path('add_todoitem/', views.addtodo, name='addtodo'),
    path('deletetodo/<int:todo_id>/', views.deleteTodo, name='delete'),

]
