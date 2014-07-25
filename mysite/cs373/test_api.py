from rest_framework.test import APITestCase
from cs373.models import *
from rest_framework import status


class StagesAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(name="new stage")
		self.stage.save()

	def tearDown(self):
		self.stage.delete()

	def testStageGet(self):
		response = self.client.get("/api/stages/1/", format="application/json")
		self.assertEqual(status.HTTP_200_OK, response.status)

	def testStageGet2(self):
		response = self.client.get("/api/stages/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status)
	
	def testPost(self):
		response = self.clent.post("/api/stages/1/", {'stage':1})
		self.assertEqual(status.HTTP_204_NO_CONTENT, response.status)

class ArtistAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(name="new stage")
		self.stage.save()
		self.artist = Artist(stage=stage, name="new artist")

	def tearDown(self):
		self.artist.delete()

	def testStageGet(self):
		response = self.client.get("/api/artists/1/", format="application/json")
		self.assertEqual(status.HTTP_200_OK, response.status)

	def testStageGet2(self):
		response = self.client.get("/api/artists/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status)
	
	def testPost(self):
		response = self.clent.post("/api/artists/1/", {'artist':1})
		self.assertEqual(status.HTTP_204_NO_CONTENT, response.status)

class SponsorsAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(name="new stage")
		self.stage.save()
		self.sponsor = Sponsor(stage = stage, name = "new sponsor")
		self.sponsor.save()

	def tearDown(self):
		self.stage.delete()

	def testStageGet(self):
		response = self.client.get("/api/sponsors/1/", format="application/json")
		self.assertEqual(status.HTTP_200_OK, response.status)

	def testStageGet2(self):
		response = self.client.get("/api/sponsors/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status)
	
	def testPost(self):
		response = self.clent.post("/api/sponsors/1/", {'sponsor':1})
		self.assertEqual(status.HTTP_204_NO_CONTENT, response.status)
