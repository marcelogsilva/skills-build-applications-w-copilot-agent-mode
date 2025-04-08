# Arquivo de visualizações para o projeto Octofit Tracker
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from django.conf import settings
from rest_framework.response import Response

class APIEndpointSuffixMixin:
    def get_api_suffix(self):
        return f"https://{settings.ALLOWED_HOSTS[-1]}/api/"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

# Example usage in a view
class ExampleView(APIEndpointSuffixMixin, viewsets.ViewSet):
    def list(self, request):
        api_suffix = self.get_api_suffix()
        return Response({"api_suffix": api_suffix})
