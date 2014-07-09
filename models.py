
from django.db import models


class Stage(models.Model):
    name            = models.CharField(max_length=400, unique=True)
    #sponsor        = models.ForeignKey(Sponsor)

    def get_url(self):
        return "/stages/%s/" % self.name

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name            = models.CharField(max_length=400)
    #sponsor_pic    = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    business_type   = models.CharField(max_length=400)
    website         = models.CharField(max_length=400)
    stage           = models.ForeignKey(Stage, blank=True, null=True)

    def get_url(self):
        return "/sponsors/%s/" % self.name

    def __str__(self):
        return self.name

class Artist(models.Model):
    name            = models.CharField(max_length=400, unique=True)
    label           = models.CharField(max_length=400)
    origin          = models.CharField(max_length=400)
    website         = models.CharField(max_length=400)
    genre           = models.CharField(max_length=400)
    stage           = models.ForeignKey(Stage)

    def get_url(self):
        return "/artists/%s/" % self.name

    def __str__(self):
        return self.name

class Photo(models.Model):
    #artist_pic     = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    file_name       = models.CharField(max_length=400)
    artist          = models.ForeignKey(Artist)

    def __str__(self):
        return self.file_name

class Member(models.Model):
    first_name      = models.CharField(max_length=400)
    last_name       = models.CharField(max_length=400)
    artist          = models.ForeignKey(Artist)

    def __str__(self):
        ret_str = self.first_name
        if(self.last_name):
            ret_str += " " + self.last_name
        return ret_str

class Event (models.Model):
    name        = models.CharField(max_length=400)
    location    = models.CharField(max_length=400)
    sponsor     = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name
