from django.db import models

"""
Three Main Entities
..that we are modeling the Austin City Limits Festival with
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
    industry            = models.CharField(max_length=255)

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
    name             = models.CharField(max_length=255, unique=True)
    label            = models.CharField(max_length=255)
    genre            = models.CharField(max_length=255)
    origin           = models.CharField(max_length=255)

    def __str__(self):
        """
        returns name
        """
        return self.name

"""
TIME
relationship classes
"""
# https://docs.djangoproject.com/en/1.6/ref/models/instances/#django.db.models.Model

class stage_sponsor_yr(models.Model):
    """
    create with method not the constructor
    """
    stage           = models.ForeignKey(Stage)
    sponsor         = models.ForeignKey(Sponsor)
    date            = models.DateField()      #datetime
    key             = models.CharField(max_length=255, unique=True)


    @classmethod
    def create(self, stage, sponsor, date):
        """
        For initialization of the primary key, Django doesn't support multi-column pk's.
        This is needed to enforce the data integrity between sponsors and stages in relation to time.
        """
        assert type(stage) == Stage
        assert type(sponsor) == Sponsor

        pkey=str(sponsor.id)+str(date.year)
        instance=self(stage=stage, sponsor=sponsor, date=date, key=pkey)
        return instance

    def get_yr(self):
        return self.date.year

class stage_artist_yr(models.Model):
    """
    For initialization of the primary key, Django doesn't support multi-column pk's.
    This is needed to enforce the data integrity between artists and stages in relation to time.
    """
    stage           = models.ForeignKey(Stage)
    artist          = models.ForeignKey(Artist)
    date            = models.DateField()      #datetime
    key             = models.CharField(max_length=255, unique=True)

    @classmethod
    def create(self, stage, artist, date):
        """
        For initialization of the primary key, Django doesn't support multi-column pk's.
        This is needed to enforce the data integrity between sponsors and stages in relation to time.
        ex: relationship=stage_artist_yr.create(stage, artist, (datetime) yr)
        """

        assert type(stage) == Stage
        assert type(artist) == Artist

        pkey=str(artist.id)+str(date.year)
        instance=self(stage=stage, artist=artist, date=date,key=pkey)
        return instance

    def get_yr(self):
        return self.date.year

"""
MEDIA
info for dynamic webpages
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

class ArtistMedia(Media):
    artist           = models.ForeignKey(Artist, unique=True)


class StageMedia(Media):
    name            = models.CharField(max_length=42) #Derivable
    year            = models.DateField()           #datetime
    stage           = models.ForeignKey(Stage)


class SponsorMedia(Media):
    sponsor      = models.ForeignKey(Sponsor, unique=True)


