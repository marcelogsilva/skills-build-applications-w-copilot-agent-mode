from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data_module import get_test_data

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Load test data
        data = get_test_data()

        # Create users
        users = {}
        for user_data in data['users']:
            user = User.objects.create(**user_data)
            users[user_data['username']] = user

        # Create teams
        for team_data in data['teams']:
            team = Team.objects.create(name=team_data['name'])
            team.members.set([users[username] for username in team_data['members']])

        # Create activities
        for activity_data in data['activities']:
            Activity.objects.create(user=users[activity_data['user']], **{k: v for k, v in activity_data.items() if k != 'user'})

        # Create leaderboard entries
        for leaderboard_data in data['leaderboard']:
            Leaderboard.objects.create(user=users[leaderboard_data['user']], score=leaderboard_data['score'])

        # Create workouts
        for workout_data in data['workouts']:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))