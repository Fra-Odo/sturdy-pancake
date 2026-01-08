from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='test'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test'),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test'),
        ]

        Activity.objects.create(user='ironman', type='run', duration=30)
        Activity.objects.create(user='spiderman', type='cycle', duration=45)
        Activity.objects.create(user='batman', type='swim', duration=60)
        Activity.objects.create(user='superman', type='run', duration=50)

        Leaderboard.objects.create(user='ironman', points=100)
        Leaderboard.objects.create(user='spiderman', points=90)
        Leaderboard.objects.create(user='batman', points=110)
        Leaderboard.objects.create(user='superman', points=120)

        Workout.objects.create(name='Full Body', description='Pushups, squats, lunges')
        Workout.objects.create(name='Cardio', description='Running, cycling, swimming')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
