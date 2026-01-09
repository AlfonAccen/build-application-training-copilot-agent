from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(username="testuser", email="test@example.com", first_name="Test", last_name="User", team=team)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.team.name, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="TeamX", description="A team")
        self.assertEqual(team.name, "TeamX")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="actuser", email="act@example.com", first_name="Act", last_name="User")
        activity = Activity.objects.create(user=user, activity_type="Run", duration=30, calories_burned=300, date="2024-01-01")
        self.assertEqual(activity.activity_type, "Run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Cardio", description="Cardio workout", difficulty="Medium", duration=45)
        self.assertEqual(workout.name, "Cardio")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="LB Team")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertEqual(leaderboard.total_points, 100)
