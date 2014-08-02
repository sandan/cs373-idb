from django.db import models

"""
Three Main Entities
"""

class Stage(models.Model):
    """
    Stages are physical locations on the acl festival map:
    see theaustinites.pythonanywhere.com/stages/

    locations are mappings from the physical stage to an integer
    """
    location        = models.PositiveSmallIntegerField(unique=True)
    name            = models.CharField(max_length=42) #Derivable depending on year, not unique b/c of year
    year            = models.DateField() 
    
    components      = models.ForeignKey(Media, unique=True)
    
    def __str__(self):
        """
        returns location
        """
        return self.location

class Sponsor(models.Model):
    """
    A Sponsor is an entity that purchases a stage
    for Music Artists to play on.
    """
    name            = models.CharField(max_length=255, unique=True)
    components   = models.ForeignKey(Media, unique=True)
    
    def __str__(self):
        """
        returns name
        """
        return self.name

class Artist(models.Model):
    """
    An Artist is an entity that plays on a sponsored stage
    """
    name            = models.CharField(max_length=255, unique=True)
    genre            = models.CharField(max_length=255)
    label            = models.CharField(max_length=255)
    
    components       = models.ForeignKey(Media, unique=True)
    
    def __str__(self):
        """
        returns name
        """
        return self.name

"""
TIME
"""
class stage_sponsor_yr(models.Model):
    stage           = models.ForeignKey(Stage)
    sponsor         = models.ForeignKey(Sponsor)
    year            = models.DateField()

    def get_yr(self):
        return self.year

class stage_artist_yr(models.Model):
    stage           = models.ForeignKey(Stage)
    artist          = models.ForeignKey(Artist)
    year            = models.DateField()

    def get_yr(self):
        return self.year

"""
MEDIA
"""
class Media(models.Model):
"""
Media resource for Artist, Sponsor, Stage
"""
    
    bio             = models.TextField()
    photo           = models.URLField(max_length=255)
    youtube         = models.URLField(max_length=255)
    video           = models.URLField(max_length=255)
    youtubevideo    = models.URLField(max_length=255)
    twitter         = models.URLField(max_length=255)
    twitterwidget   = models.URLField(max_length=255)
    facebook        = models.URLField(max_length=255)
    webpage         = models.URLField(max_length=255)

    def __str__(self):
        return self.webpage
