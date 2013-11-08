from django.db import models

class Artist(models.Model):
    #normally I would name these vars by types ... but since db field names ... and given def to right, ... not
    full_name = models.CharField(max_length=70)
    soundcloud_id = models.CharField(max_length=70) 
    youtube_id = models.CharField(max_length=70) 
    facebook_id = models.CharField(max_length=70) 
    twitter_id = models.CharField(max_length=70) 
    email_addr = models.CharField(max_length=70) 
    slogan = models.CharField(max_length=70)
    def __unicode__(self):
        return self.full_name

def add_artist(sFullName, dDictArgs):
  aArtistToInsert = Artist(full_name=sFullName, **dDictArgs) #required fields?
  aArtistToInsert.save()

def test_add_artists():
  aaArtists = Artist.objects.filter(full_name__exact="djlisan")
  if len(aaArtists) == 1:
    #expected case
    aaArtists[0].delete()
  elif len(aaArtists) > 1:
    print('more than one match for my friend the dj, shouldnt happen?')
    return
  #0 case means Ive not run this yet. was going to do it manually first, but why not test the test.
  dDictArgs = {'soundcloud_id':'dj-lisan', 
               'youtube_id':'', 
               'facebook_id':'DjLisan', 
               'twitter_id':'djlisan', 
               'email_addr':'djlisan@gmail.com', 
               'slogan':'Dance Floor Breaker'}
  add_artist('djlisan', dDictArgs)
  aaArtists = Artist.objects.filter(full_name__exact="djlisan")
  if len(aaArtists) != 1:
    print('inserting djlisan yielded 0 or multiple rows, problems')
  return

class Song(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    link = models.TextField()
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.headline

# want to be able to click any of the links to go to an artist's pages
# but also want to be able to open to view on the page any of those things. 
# what can you do from there besides watching the preselected youtube playlist, ... 
#   add to it, mash it, 

# really need to work on frontpage, elevator pitch. 
#   after elevator pitch more details. 
#  note to self  members = models.ManyToManyField(Person, through='Membership')

