from django.db import models

class Artist(models.Model):
    #normally I would name these vars by types ... but since db field names ... and given def to right, ... not
    full_name = models.CharField(max_length=70)
    #could probably be more efficient here, need to check details
    soundcloud_id = models.CharField(max_length=70) 
    youtube_id = models.CharField(max_length=70) 
    facebook_id = models.CharField(max_length=70) 
    twitter_id = models.CharField(max_length=70) 
    email_addr = models.CharField(max_length=70) 
    def __unicode__(self):
        return self.full_name

class Song(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    link = models.TextField()
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.headline

