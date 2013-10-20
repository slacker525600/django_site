from django.db import models

class Artist(models.Model):
    full_name = models.CharField(max_length=70)

    def __unicode__(self):
        return self.full_name

class Song(models.Model):
    pub_date = models.DateField()
    title = models.CharField(max_length=200)
    link = models.TextField()
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.headline

