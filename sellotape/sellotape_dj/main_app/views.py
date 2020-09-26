from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Stream, Profile


def index(request):
    return render(request, 'sellotape/index.html')


def user(request, username):
    # Get the profile for the passed username or raise 404 if not found.
    # If found, retrieve the related profile streams.
    profile = get_object_or_404(Profile, user__username=username)
    streams = Stream.objects.filter(author=profile)

    # Check if there is a live stream at the moment.
    live_stream = None
    now = timezone.now()
    for s in streams:
        ongoing = s.ends_on == None or s.ends_on >= now
        if ongoing and s.airs_on <= now:
            live_stream = s
            break

    # Filter streams data based on the current time of serving the page.
    future_streams = [s for s in streams if s.airs_on > now]
    previous_streams = [s for s in streams if s not in future_streams]

    if live_stream in previous_streams:
        previous_streams.remove(live_stream)

    context = {
        'profile': profile,
        'future_streams': future_streams,
        'previous_streams': previous_streams,
        'live_stream': live_stream,
    }
    return render(request, 'user.html', context)