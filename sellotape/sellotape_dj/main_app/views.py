from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Stream, Profile, UserFollower
from django.db.models import Count

def landing(request):
    return render(request, 'landing.html')


def user(request, username):
    # genres = Stream.objects.values_list('genre', flat=True)

    genres = Stream.objects.values('genre').annotate(Count('genre'))  # This will return all the unique last_names
    values = dict((genre['genre'], Stream.objects.all().filter(genre=genre['genre'])) for genre in genres)
    # This will create a dictionary where the keys are all the unique genres and the values are querysect of all the values that have that genre

    top_rated = UserFollower.objects.annotate(num_followers=Count('follows')).order_by('-num_followers')[:5]

    return render(request, 'sellotape/user.html', {'previous_streams': values, 'future_streams': top_rated})

