
from django.db import models


class Stage(models.Model):
    """
    A reprentation of a stage
    """
    name            = models.CharField(max_length=400, unique=True)
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

    name            = models.CharField(max_length=400)
    #sponsor_pic    = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    business_type   = models.CharField(max_length=400)
    website         = models.CharField(max_length=400)
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
    name            = models.CharField(max_length=400, unique=True)
    label           = models.CharField(max_length=400)
    origin          = models.CharField(max_length=400)
    website         = models.CharField(max_length=400)
    genre           = models.CharField(max_length=400)
    bio             = models.TextField(max_length=5000)
    youtube         = models.CharField(max_length=400)
    stage           = models.ForeignKey(Stage)

    def get_url(self):
        """
        returns url
        """
        return "/artists/%s/" % self.id

    def photo(self):
        return '/static/images/artist/%s.jpg' % self.name.replace(' ','').lower()

    def __str__(self):
        """
        returns Artist name
        """
        return self.name

class Media(models.Model):
    """
    Media resource for Artist, Sponsor, Stage
    """
    
    Bio=models.TextField(max_length=5000)
    Image= models.CharField(max_length=400)
    Youtube=models.CharField(max_length=400)
    Video=models.CharField(max_length=400)
    Twitter=models.CharField(max_length=400)
    Facebook=models.CharField(max_length=400)
    Webpage=models.CharField(max_length=400)
    

    def __str__(self):
        """
        returns Photo file_name
        """
        return self.file_name

"""
DEPRECATED
class Member(models.Model):
    
    
    
    first_name      = models.CharField(max_length=400)
    last_name       = models.CharField(max_length=400)
    artist          = models.ForeignKey(Artist)

    def __str__(self):
    
    
    
        ret_str = self.first_name
        if(self.last_name):
            ret_str += " " + self.last_name
        return ret_str


"""
