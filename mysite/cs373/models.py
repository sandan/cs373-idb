
from django.db import models


class Stage(models.Model):
    """
    A reprentation of a stage
    """
    name            = models.CharField(max_length=255, unique=True)
    #sponsor        = models.ForeignKey(Sponsor)

    # def get_name(self):
    #     return self.name

    def get_url(self):
        """
        returns url
        """
        return "/stages/%s/" % self.id

    def __str__(self):
        """
        returns stage name
        """
        return self.name

class Sponsor(models.Model):
    """
    A representation of a Sponsor
    """

    name            = models.CharField(max_length=255)
    business_type   = models.CharField(max_length=255)
    stage           = models.ForeignKey(Stage, blank=True, null=True)


    # def get_name(self):
    #     return self.name

    # def get_business_type(self):
    #     return self.busoness_type

    def get_url(self):
        """
        returns url
        """
        return "/sponsors/%s/" % self.id

    def img_url(self):
        return '/images/sponsor/%i.jpg' % self.name.lower().replace(' ','')

    def __str__(self):
        """
        returns Sponsor name
        """
        return self.name


class Artist(models.Model):
    """
    A representation of an artist
    """
    name            = models.CharField(max_length=255, unique=True)
    label           = models.CharField(max_length=255)
    origin          = models.CharField(max_length=255)
    genre           = models.CharField(max_length=255)
    stage           = models.ForeignKey(Stage)

    def get_url(self):
        """
        returns url
        """
        return "/artists/%s/" % self.id

   # def photo(self):
    #    return '/static/images/artist/%s.jpg' % self.name.replace(' ','').lower()

    def __str__(self):
        """
        returns Artist name
        """
        return self.name

class Media(models.Model):
    """
    Media resource for Artist, Sponsor, Stage
    """

    Bio=models.CharField(max_length=255)
    Photo= models.CharField(max_length=255)
    Youtube=models.CharField(max_length=255)
    Video=models.CharField(max_length=255)
    Twitter=models.CharField(max_length=255)
    Facebook=models.CharField(max_length=255)
    # holds the html code for twitter timeline widget
    twitterwidget = models.CharField(max_length=255)
    # holds the src of youtube video
    # ex. src='{{media.youtubevideo}}'
    youtubevideo = models.CharField(max_length=255)
    Webpage=models.CharField(max_length=255)

    def __str__(self):
        """
        returns Webpage link
        """
        return self.Webpage

class ArtistMedia(Media):
    ar = models.ForeignKey(Artist)

class StageMedia(Media):
    st = models.ForeignKey(Stage)

class SponsorMedia(Media):
    sp = models.ForeignKey(Sponsor)

"""
DEPRECATED
class Member(models.Model):



    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    artist          = models.ForeignKey(Artist)

    def __str__(self):



        ret_str = self.first_name
        if(self.last_name):
            ret_str += " " + self.last_name
        return ret_str


"""
