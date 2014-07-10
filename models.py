
#from django.db import models


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
    stage           = models.ForeignKey(Stage)

    def get_url(self):
        """
        returns url
        """
        return "/artists/%s/" % self.id

    def __str__(self):
        """
        returns Artist name
        """
        return self.name

class Photo(models.Model):
    """
    A representation of a Photo
    """
    #artist_pic     = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    file_name       = models.CharField(max_length=400)
    artist          = models.ForeignKey(Artist)

    def __str__(self):
        """
        returns Photo file_name
        """
        return self.file_name

class Member(models.Model):
    """
    A representation of a Model
    """
    first_name      = models.CharField(max_length=400)
    last_name       = models.CharField(max_length=400)
    artist          = models.ForeignKey(Artist)

    def __str__(self):
        """
        Returns the name of the member
        """
        ret_str = self.first_name
        if(self.last_name):
            ret_str += " " + self.last_name
        return ret_str


