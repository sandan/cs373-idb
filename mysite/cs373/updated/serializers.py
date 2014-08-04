from rest_framework import serializers
from times import models

class StageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Stage
		fields= ('location',)

class SponsorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Sponsor
		fields=('id','name','industry')

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Artist
		fields=('id','name','genre','label','origin')

class ArtistMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ArtistMedia
		fields = ('artist','bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')

#TODO
class StageMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.StageMedia
		fields = ('name','bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')


class SponsorMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.SponsorMedia
		fields = ('sponsor','bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')

