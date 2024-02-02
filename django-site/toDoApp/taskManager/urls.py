from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("handle/<int:task_id>/", views.handle_request, name="handle_request"),
]
