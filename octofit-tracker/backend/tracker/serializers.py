from rest_framework import serializers
from .models import Team, UserProfile, Activity, Workout, Leaderboard


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'created_at']


class UserProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'display_name', 'team']


class ActivitySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'distance_km', 'created_at']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'created_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'points', 'created_at']
