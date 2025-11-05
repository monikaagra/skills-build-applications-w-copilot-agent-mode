from django.core.management.base import BaseCommand
from tracker.models import UserProfile, Team, Activity

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        for obj in UserProfile.objects.all():
            if obj.id:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.id:
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = UserProfile.objects.create(username='ironman', display_name='Iron Man', team=marvel)
        captain = UserProfile.objects.create(username='cap', display_name='Captain America', team=marvel)
        batman = UserProfile.objects.create(username='batman', display_name='Batman', team=dc)
        superman = UserProfile.objects.create(username='superman', display_name='Superman', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, activity_type='run', duration_minutes=30, distance_km=5)
        Activity.objects.create(user=captain, activity_type='swim', duration_minutes=45, distance_km=2)
        Activity.objects.create(user=batman, activity_type='bike', duration_minutes=60, distance_km=20)
        Activity.objects.create(user=superman, activity_type='other', duration_minutes=20, distance_km=None)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
