from django.db import models
from django.forms import ModelForm
from django import forms


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200, default="No Description")
    task_priority = models.IntegerField(default=0)
    task_status = models.CharField(max_length=200, default="Not Started")

    def __str__(self):
        return self.task_name


class TaskAddForm(ModelForm):
    class Meta:
        model = Task
        fields = ["task_name", "task_description", "task_priority", "task_status"]


class TaskDisplayForm(forms.Form):
    task_name = forms.CharField(max_length=200)
    id = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        name = kwargs.pop("task_name")
        id = kwargs.pop("id")
        super(TaskDisplayForm, self).__init__(*args, **kwargs)
        self.fields["task_name"].initial = name
        self.fields["id"].initial = id
