from django.shortcuts import render, redirect
from django.urls import reverse
from taskManager.models import Task, TaskAddForm, TaskDisplayForm


# Create your views here.
def index(request):

    if request.method == "POST":
        form = TaskAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
    else:
        form = TaskAddForm()
    task_list = [
        TaskDisplayForm(task_name=task.task_name, id=task.id)
        for task in Task.objects.all()
    ]
    context_dict = {"task_list": task_list, "form": form}
    return render(request, "taskManager/index.html", context=context_dict)


def handle_request(request, task_id):
    if request.method == "POST":
        button_value = request.POST.get("action")
        if button_value == "Delete":
            Task.objects.get(id=task_id).delete()
    return redirect(reverse("index"))
