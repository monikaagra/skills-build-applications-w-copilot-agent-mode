from django.db import models
from djongo import models as djongo_models


class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, editable=False)
    username = models.CharField(max_length=100, unique=True)
    display_name = models.CharField(max_length=150, blank=True)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username


class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('run', 'Run'),
        ('bike', 'Bike'),
        ('swim', 'Swim'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(UserProfile, related_name='activities', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} ({self.duration_minutes}m)"

    class Workout(models.Model):
        id = djongo_models.ObjectIdField(primary_key=True, editable=False)
        name = models.CharField(max_length=100, unique=True)
        description = models.TextField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name

    class Leaderboard(models.Model):
        id = djongo_models.ObjectIdField(primary_key=True, editable=False)
        user = models.ForeignKey(UserProfile, related_name='leaderboard_entries', on_delete=models.CASCADE)
        points = models.PositiveIntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user.username} - {self.points} pts"
