from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('current/', todo_views.currenttodos, name = "currenttodos"),
    path('create/', todo_views.createtodo, name = "createtodo"),
    path('completed/', todo_views.completedtodos, name = "completedtodos"),
    path('todo/<int:todo_pk>/', todo_views.viewtodo, name = "viewtodo"),
    path('', todo_views.home, name = "home"),
    path('todo/<int:todo_pk>/complete/', todo_views.completetodo, name = "completetodo"),
    path('todo/<int:todo_pk>/uncomplete/', todo_views.uncompletetodo, name = "uncompletetodo"),
    path('todo/<int:todo_pk>/delete/', todo_views.deletetodo, name = "deletetodo"),
]
