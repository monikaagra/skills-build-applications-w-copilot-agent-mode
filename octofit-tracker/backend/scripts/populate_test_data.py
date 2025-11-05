"""Populate octofit_db with test data using Django ORM.

Run with the backend venv activated, e.g.:
  /path/to/venv/bin/python /path/to/octofit-tracker/backend/scripts/populate_test_data.py
"""
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from tracker.models import Team, UserProfile, Activity


def populate():
    if Team.objects.exists():
        print('Test data already present; skipping populate.')
        return

    t1 = Team.objects.create(name='Team Octo')
    t2 = Team.objects.create(name='Team Fit')

    u1 = UserProfile.objects.create(username='alice', display_name='Alice', team=t1)
    u2 = UserProfile.objects.create(username='bob', display_name='Bob', team=t1)
    u3 = UserProfile.objects.create(username='carol', display_name='Carol', team=t2)

    Activity.objects.create(user=u1, activity_type='run', duration_minutes=25, distance_km=4.2)
    Activity.objects.create(user=u1, activity_type='bike', duration_minutes=40, distance_km=15.0)
    Activity.objects.create(user=u2, activity_type='run', duration_minutes=30, distance_km=5.0)
    Activity.objects.create(user=u3, activity_type='swim', duration_minutes=50, distance_km=None)

    print('Populated test data: teams=%d users=%d activities=%d' % (
        Team.objects.count(), UserProfile.objects.count(), Activity.objects.count()))


if __name__ == '__main__':
    populate()
