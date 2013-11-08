from mlarble.models import Artist
from django.shortcuts import render_to_response

def artists(request):
    aaArtists = Artist.objects.all()
    return render_to_response('artists.html', {'aArtists': aaArtists})
def home(request):
    return render_to_response('homepage.html', {})
def artist(request):
    sName = 'djlisan' # will want to use request 
    aArtist = Artist.objects.filter(full_name__exact=sName)
    return render_to_response('artist.html', {'aArtist':aArtist})

