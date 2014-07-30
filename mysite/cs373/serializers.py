from rest_framework import serializers
from cs373 import models

class StageSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Stage
		fields = ('id', 'name')

class SponsorSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Sponsor
		fields = ('id', 'name', 'business_type', 'stage')

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Artist
		fields = ('id', 'name', 'label', 'origin', 'genre', 'stage')

class ArtistMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ArtistMedia
		fields = ('ar','bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')

class StageMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.StageMedia
		fields = ('st', 'bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')

class SponsorMediaSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.SponsorMedia
		fields = ('sp', 'bio', 'photo', 'youtube', 'video', 'twitter', 'facebook', 'twitterwidget', 'youtubevideo', 'webpage')
