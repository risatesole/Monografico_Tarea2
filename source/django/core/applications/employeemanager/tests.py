from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Team, Todo

class TeamViewsTest(TestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="123")
        self.other_user = User.objects.create_user(username="other", password="123")

        # Login
        self.client.login(username="testuser", password="123")

        # Create a team
        self.team = Team.objects.create(
            name="Team A",
            description="Desc",
            submitted_by=self.user
        )

    def test_teambase_returns_user_teams(self):
        response = self.client.get(reverse("teambase"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Team A")

    def test_team_workspace_get(self):
        response = self.client.get(
            reverse("team_workspace", args=[self.team.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Team A")

    def test_team_workspace_post_creates_todo(self):
        response = self.client.post(
            reverse("team_workspace", args=[self.team.id]),
            {"title": "New Task"}
        )

        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Todo.objects.count(), 1)

    def test_team_workspace_other_user_forbidden(self):
        other_team = Team.objects.create(
            name="Other Team",
            submitted_by=self.other_user
        )

        response = self.client.get(
            reverse("team_workspace", args=[other_team.id])
        )

        self.assertEqual(response.status_code, 404)

    def test_create_team(self):
        response = self.client.post(
            reverse("create_team"),
            {"name": "New Team", "description": "Test"}
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Team.objects.filter(name="New Team").exists())

    def test_delete_team(self):
        response = self.client.post(
            reverse("delete_team", args=[self.team.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Team.objects.filter(id=self.team.id).exists())

    def test_delete_task(self):
        task = Todo.objects.create(
            title="Task",
            team=self.team,
            assigned_to=self.user
        )

        response = self.client.post(
            reverse("delete_task", args=[task.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=task.id).exists())
