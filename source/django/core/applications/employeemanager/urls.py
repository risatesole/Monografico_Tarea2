from django.urls import path
from .views import teambase, create_team, delete_team, team_workspace, delete_task

urlpatterns = [
    path("", teambase, name="teambase"),
    path("create-team/", create_team, name="create_team"),
    path("delete-team/<int:team_id>/", delete_team, name="delete_team"),
    path("team/<int:team_id>/workspace/", team_workspace, name="team_workspace"),
    path("delete-task/<int:task_id>/", delete_task, name="delete_task"),
]