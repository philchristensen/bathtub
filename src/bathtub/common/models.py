from django.db import models

class Artist(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __unicode__(self):
        return self.date

class Venue(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __unicode__(self):
        return self.date

class Tour(models.Model):
    artist = models.ForeignKey(Artist, related_name='tours')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    year = models.IntegerField()
    
    def __unicode__(self):
        return self.date

class Show(models.Model):
    tour = models.ForeignKey(Tour, related_name='shows')
    date = models.DateField()
    
    def __unicode__(self):
        return self.date

class Set(models.Model):
    show = models.ForeignKey(Show, related_name='sets')
    index = models.IntegerField()
    
    def __unicode__(self):
        return self.date

class Song(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    is_cover = models.BooleanField(default=False)
    original_artist = models.ForeignKey(Artist, blank=True, null=True)
    
    def __unicode__(self):
        return self.date

