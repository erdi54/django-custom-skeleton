from django.urls import path
from .webhook.git import git_hook
# for authentication
urlpatterns = [
    path("webhook/git_hook", git_hook, name="pull_repo"),
]

