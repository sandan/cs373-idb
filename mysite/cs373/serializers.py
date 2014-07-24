"""
from rest_framework import serializers
from cs373.models import Stage, Sponsor, Artist, Photo, Member

class StageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stage
		fields = ('id', 'name')

class SponsorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sponsor
		fields = ('id', 'name', 'business_type', 'website', 'stage')

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = ('id', 'name', 'label', 'origin', 'website', 'genre', 'stage', 'bio', 'youtube')

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = ('id', 'file_name', 'artist')

class MemberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Member
		fields = ('id', 'first_name', 'last_name', 'artist')
"""