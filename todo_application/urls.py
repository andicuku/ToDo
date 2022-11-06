from django.urls import path

from todo_application.views import add, index, delete, finish, delete_all, edit_view, edit, finish_subtask, \
    create_subtask, delete_subtask

urlpatterns = [
    path('', index, name="index"),
    path("add/", add),
    path("delete/<int:pk>/", delete),
    path("finish/<int:pk>/", finish),
    path("delete_all/", delete_all),
    path("edit/<int:pk>/", edit),
    path("edit_view/<int:pk>/", edit_view, name="edit_view"),
    path("finish_subtask/<int:pk>/", finish_subtask),
    path("create_subtask/<int:pk>/", create_subtask),
    path("delete_subtask/<int:pk>/", delete_subtask),
]
