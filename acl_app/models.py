
from django.db import models


class Stage(models.Model):
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=400)
    #sponsor_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    business_type = models.CharField(max_length=400)
    website = models.CharField(max_length=400)
    stage = models.ForeignKey(Stage, blank=True, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=400, unique=True)
    label = models.CharField(max_length=400)
    origin = models.CharField(max_length=400)
    website = models.CharField(max_length=400)
    genre = models.CharField(max_length=400)
    stage = models.ForeignKey(Stage)

    def __str__(self):
        return self.name

class Artist_Photo(models.Model):
    #artist_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    file_name = models.CharField(max_length=400)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return self.file_name

class Artist_Member(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    artist = models.ForeignKey(Artist)

    def __str__(self):
        ret_str = first_name
        if(last_name):
            ret_str += " " + last_name
        return ret_str

