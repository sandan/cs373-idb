from rest_framework.test import APITestCase
from cs373.models import *
from rest_framework import status


class StageMediaAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(name="new stage")
		self.stage.save()
		self.stage_media = StageMedia(bio="stage bio", st=self.stage)
		self.stage_media.save()
		self.url = "/api/stages/1/media/"
		self.bad_url = "/api/stages/2/media/"
		self.data = {"bio": "new stage bio", "st":1}

	def tearDown(self):
		self.stage_media.delete()
		self.stage.delete()

	def test_stage_media_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_stage_media_bad_get(self):
		response = self.client.get(self.bad_url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_stage_media_post(self):
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class ArtistMediaAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(name="new stage")
		self.stage.save()
		self.artist = Artist(name="new artist", stage=self.stage)
		self.artist.save()
		self.artist_media = ArtistMedia(bio="artist bio", ar=self.artist)
		self.artist_media.save()
		self.url = "/api/artists/1/media/"
		self.bad_url = "/api/artists/2/media/"
		self.data = {"bio": "new artist bio", "ar":1}

	def tearDown(self):
		self.artist_media.delete()
		self.artist.delete()
		self.stage.delete()

	def test_artist_media_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_artist_media_bad_get(self):
		response = self.client.get(self.bad_url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_artist_media_post(self):
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class SponsorMediaAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(name="new stage")
		self.stage.save()
		self.sponsor = Sponsor(name="new sponsor", stage=self.stage)
		self.sponsor.save()
		self.sponsor_media = SponsorMedia(bio="sponsor bio", sp=self.sponsor)
		self.sponsor_media.save()
		self.url = "/api/sponsors/1/media/"
		self.bad_url = "/api/sponsors/2/media/"
		self.data = {"bio": "new sponsor bio", "ar":1}

	def tearDown(self):
		self.sponsor_media.delete()
		self.sponsor.delete()
		self.stage.delete()

	def test_sponsor_media_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_sponsor_media_bad_get(self):
		response = self.client.get(self.bad_url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_sponsor_media_post(self):
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)



