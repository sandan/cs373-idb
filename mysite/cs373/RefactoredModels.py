from django.db import models

"""
Three Main Entities
"""

class Stage(models.Model):
    """
    Stages are physical locations on the acl festival map:
    see theaustinites.pythonanywhere.com/stages/

    Locations are mappings from the physical stage to an integer.
    For any single year, a stage will have one sponsor and many artists playing.
    For different years, a stage can potentially have different sponsors and many artists playing.
    """
    location            = models.PositiveSmallIntegerField(unique=True)
    def __str__(self):
        """
        returns location
        """
        return str(self.location)

class Sponsor(models.Model):
    """
    A Sponsor is an entity that purchases a stage
    for Music Artists to play on.
    For any single year, a sponsor can only sponsor one stage.
    For many different years a sponsor could potentially sponsor
    a different stage (location).
    """
    name            = models.CharField(max_length=255, unique=True)
    def __str__(self):
        """
        returns name
        """
        return self.name

class Artist(models.Model):
    """
    An Artist is an entity that plays on a sponsored stage.
    For any single year, an artist can only play on one stage.
    For multiple different years, an artist may play on potentially >1 stage.
    """
    name            = models.CharField(max_length=255, unique=True)
    def __str__(self):
        """
        returns name
        """
        return self.name

"""
TIME
"""
# https://docs.djangoproject.com/en/1.6/ref/models/instances/#django.db.models.Model

class stage_sponsor_yr(models.Model):
    """
    create with method not the constructor
    """
    stage           = models.ForeignKey(Stage)
    sponsor         = models.ForeignKey(Sponsor)
    year            = models.DateField()      #datetime
    key             = models.CharField(max_length=255, primary_key=True)


    @classmethod
    def create(self, stage, sponsor, year):
        """
        For initialization of the primary key, Django doesn't support multi-column pk's.
        This is needed to enforce the data integrity between sponsors and stages in relation to time.
        """
        pkey=str(sponsor.id)+str(year.year)
        instance=self(stage=stage, sponsor=sponsor, year=year, key=pkey)
        return instance

    def get_yr(self):
        return self.year

class stage_artist_yr(models.Model):
    """
    For initialization of the primary key, Django doesn't support multi-column pk's.
    This is needed to enforce the data integrity between artists and stages in relation to time.
    """
    stage           = models.ForeignKey(Stage)
    artist          = models.ForeignKey(Artist)
    year            = models.DateField()      #datetime
    key             = models.CharField(max_length=255, unique=True, primary_key=True)

    def get_yr(self):
        return self.year

    @classmethod
    def create(self, stage, artist, year):
        """
        For initialization of the primary key, Django doesn't support multi-column pk's.
        This is needed to enforce the data integrity between sponsors and stages in relation to time.
        ex: relationship=stage_artist_yr.create(stage, artist, (datetime) yr)
        """
        pkey=str(artist.id)+str(year.year)
        instance=self(stage=stage, artist=artist, year=year,key=pkey)
        return instance

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

class ArtistMedia(models.Model):
    artist           = models.ForeignKey(Artist, unique=True)
    components       = models.ForeignKey(Media, unique=True)

class StageMedia(models.Model):
    name            = models.CharField(max_length=42) #Derivable 
    year            = models.DateField()           #datetime
    stage           = models.ForeignKey(Stage)
    components      = models.ForeignKey(Media, unique=True)

class SponsorMedia(models.Model):
    sponsor      = models.ForeignKey(Sponsor, unique=True)
    components   = models.ForeignKey(Media, unique=True)
"""
alternative time model
"""
class Year(models.Model):
    year        = models.DateField()
    stage       = models.ForeignKey(Stage)
    sponsor     = models.ForeignKey(Sponsor)
    artist      = models.ForeignKey(Artist)
    key         = models.CharField(max_length=99, primary_key=true)
    
    @classmethod
    def create(self, stage, sponsor, artist, yr):
        """
        For initialization of the primary key, Django doesn't support multi-column pk's.
        This is needed to enforce the data integrity between sponsors and stages in relation to time.
        ex: relationship=stage_artist_yr.create(stage, artist, (datetime) yr)
        """
        self.stage=stage
        self.artist=artist
        self.sponsor=sponsor
        self.year=yr
        self.key=str(sponsor.id)+str(artist.id)+str(yr.year)
