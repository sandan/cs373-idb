
from django.db import models

# Create your models here.

class Sponsor(models.Model):
    name = models.CharField(max_length=400)
    #sponsor_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    business_type = models.CharField(max_length=400)
    website = models.CharField(max_length=400)
    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=400)
    sponsor = models.OneToOneField(Sponsor)
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=400)
    label = models.CharField(max_length=400)
    origin = models.CharField(max_length=400)
    website = models.CharField(max_length=400)
    genre = models.CharField(max_length=400)
    stage = models.ForeignKey(Stage)
    def __str__(self):
        return self.name

class Band_Photo(models.Model):
    #artist_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    file_name = models.CharField(max_length=400)
    artist_id = models.ForeignKey(Artist)
    def __str__(self):
        return self.file_name

class Band_Member(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    band = models.ForeignKey(Artist)
    def __str__(self):
        return self.first_name + " " + self.last_name

