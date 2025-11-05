from django.test import TestCase
from .models import Team, UserProfile, Activity


class TrackerModelsTest(TestCase):
    def test_create_team_user_activity(self):
        team = Team.objects.create(name='Testers')
        user = UserProfile.objects.create(username='alice', display_name='Alice', team=team)
        activity = Activity.objects.create(user=user, activity_type='run', duration_minutes=30, distance_km=5.0)

        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(activity.user.username, 'alice')

    def test_create_workout(self):
        from .models import Workout
        workout = Workout.objects.create(name='Cardio Blast', description='Intense cardio workout')
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(workout.name, 'Cardio Blast')

    def test_create_leaderboard(self):
        from .models import Leaderboard
        team = Team.objects.create(name='Champions')
        user = UserProfile.objects.create(username='bob', display_name='Bob', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=150)
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(leaderboard.user.username, 'bob')
