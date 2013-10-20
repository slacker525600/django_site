from mlarble.models import Artist
from django.shortcuts import render_to_response

def artists(request):
    aaArtists = Artist.objects.all()
    return render_to_response('artists.html', {'aArtists': aaArtists})



