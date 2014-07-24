from rest_framework import serializers
from cs373 import models

class StageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Stage
		fields = ('name',)

class SponsorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Sponsor
		fields = ('name', 'business_type', 'stage')

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Artist
		fields = ('name', 'label', 'origin', 'genre', 'stage')

class ArtistMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ArtistMedia
		fields = ('bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')

class StageMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.StageMedia
		fields = ('bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')

class SponsorMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.SponsorMedia
		fields = ('bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')
