from django.shortcuts import redirect, render

from todo_application.models import ToDo, SubTasks


# Create your views here.

def index(request):
    to_do = ToDo.objects.all().order_by("-id")
    subtasks = SubTasks.objects.filter(completed=False).order_by("-id")
    return render(request=request, context={'to_do': to_do, "subtasks": subtasks}, template_name="index.html")


def add(request):
    if request.method == "POST":
        if not request.POST.get("title"):
            return render(request=request, template_name="index.html", context={"error": "Title is required"})
        ToDo.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            completed=False
        )
    return redirect("index")


def delete(request, pk):
    ToDo.objects.get(pk=pk).delete()
    return redirect("index")


def finish(request, pk):
    todo = ToDo.objects.get(pk=pk)
    subtasks = todo.subtasks.all()
    if subtasks:
        subtasks.filter(completed=False).update(completed=True)
    todo.completed = not todo.completed
    todo.save()
    return redirect("index")


def edit_view(request, pk):
    todo = ToDo.objects.get(pk=pk)
    subtasks = todo.subtasks.all().order_by("-id")
    if not todo:
        return redirect("index")
    return render(request=request, context={'todo': todo, 'subtasks': subtasks}, template_name="edit_todo.html")


def edit(request, pk):
    if request.method == "POST":
        if not request.POST.get("title"):
            return render(request=request, template_name="index.html", context={"error": "Title is required"})
        todo = ToDo.objects.get(pk=pk)
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description")
        todo.save()
    return redirect("index")


def finish_subtask(request, pk):
    subtask = SubTasks.objects.get(pk=pk)
    subtask.completed = not subtask.completed
    subtask.save()
    return redirect("edit_view", pk=subtask.todo.id)


def create_subtask(request, pk):
    if request.method == "POST":
        if not request.POST.get("title"):
            return render(request=request, template_name="index.html", context={"error": "Title is required"})
        todo = ToDo.objects.get(pk=pk)
        SubTasks.objects.create(
            title=request.POST.get("title"),
            completed=False,
            todo=todo
        )
    return redirect("edit_view", pk=pk)


def edit_subtask(request, pk):
    if request.method == "POST":
        if not request.POST.get("title"):
            return render(request=request, template_name="index.html", context={"error": "Title is required"})
        subtask = SubTasks.objects.get(pk=pk)
        subtask.title = request.POST.get("title")
        subtask.save()
        return redirect("edit_view", pk=subtask.todo.id)
    return redirect("index")


def delete_subtask(request, pk):
    subtask = SubTasks.objects.get(pk=pk)
    subtask.delete()
    return redirect("edit_view", pk=subtask.todo.id)


def delete_all(request):
    ToDo.objects.all().delete()
    return redirect("index")
