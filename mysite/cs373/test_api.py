from rest_framework.test import APITestCase
from cs373.models import Artist, Stage, Sponsor, Media, ArtistMedia, SponsorMedia, StageMedia
from rest_framework import status


class StagesAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(id = 1, name="new stage")
		self.stage.save()

	def tearDown(self):
		self.stage.delete()

	def testStageGet(self):
		response = self.client.get("/api/stages/1/", format="application/json")
		self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testStageGet2(self):
		response = self.client.get("/api/stages/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/stages/1/", {'stage':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

class ArtistAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(id=1, name="new stage")
		self.stage.save()
		self.artist = Artist(id=1, stage=self.stage, name="new artist")
		self.artist.save()

	def tearDown(self):
		self.artist.delete()

	def testStageGet(self):
		response = self.client.get("/api/artists/1/", format="application/json")
		self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testStageGet2(self):
		response = self.client.get("/api/artists/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/artists/1/", {'artist':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

class SponsorsAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(id=1, name="new stage")
		self.stage.save()
		self.sponsor = Sponsor(id=1, stage = self.stage, name = "new sponsor")
		self.sponsor.save()

	def tearDown(self):
		self.stage.delete()

	def testStageGet(self):
		response = self.client.get("/api/sponsors/1/", format="application/json")
		self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testStageGet2(self):
		response = self.client.get("/api/sponsors/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/sponsors/1/", {'sponsor':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)
