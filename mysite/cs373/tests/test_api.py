from rest_framework.test import APITestCase
from cs373.models import *
from rest_framework import status
import datetime


#/api/stages/
class StagesAllAPITest(APITestCase):

	def testValidStageGet(self):
	    response = self.client.get("/api/stages/", format="application/json")
	    self.assertEqual( len(response.data), 3 )
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testPostNotAllowed(self):
		response = self.client.post("/api/stages/1/", {'stage':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

	def setUp(self):

		self.stage1 = Stage(location = 1)
		self.stage1.save()

		self.stage2 = Stage(location = 2)
		self.stage2.save()

		self.stage3 = Stage(location = 3)
		self.stage3.save()

	def tearDown(self):
		self.stage1.delete()
		self.stage2.delete()
		self.stage3.delete()

#/api/stages/{location}
class StagesAPITest(APITestCase):

	def testValidStageGet(self):
	    response = self.client.get("/api/stages/1/", format="application/json")
	    self.assertEqual( response.data, { 'location' : 1 ,'years' : list() } )
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testInvalidStageGet(self):
		response = self.client.get("/api/stages/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPostNotAllowed(self):
		response = self.client.post("/api/stages/1/", {'stage':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

	def setUp(self):
		self.stage = Stage(location = 1)
		self.stage.save()

	def tearDown(self):
		self.stage.delete()

#/api/stages/{location}/{year}
class StagesYearAPITest(APITestCase):

	def testValidStageGet1(self):
	    response = self.client.get("/api/stages/1/2012/", format="application/json")
	    for k in response.data.keys():
	        self.assertIn(k,['year','sponsor','artists','location'])
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testValidStageGet2(self):
	    response = self.client.get("/api/stages/1/2014/", format="application/json")
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testInvalidStageGet(self):
		response = self.client.get("/api/stages/2/2013/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPostNotAllowed(self):
		response = self.client.post("/api/stages/1/", {'stage':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

	def setUp(self):
		self.stage = Stage(location = 1)
		self.stage.save()
		self.a=Artist(name='rick james')
		self.a.save()
		self.rel=stage_artist_yr.create(stage=self.stage, artist=self.a,date=datetime.date(2014,2,3))
		self.rel.save()
		self.rels=stage_artist_yr.create(stage=self.stage, artist=self.a,date=datetime.date(2012,2,3))
		self.rels.save()

	def tearDown(self):
	    self.stage.delete()
	    self.a.delete()
	    self.rel.delete()
	    self.rels.delete()

#/api/artists/{id}
class ArtistAPITest(APITestCase):
	def setUp(self):

		self.artist = Artist(id=1, name="new artist")
		self.artist.save()
		self.stage1=Stage(location=1)
		self.stage1.save()
		self.rel=stage_artist_yr.create(stage=self.stage1, artist=self.artist, date=datetime.date(2014,2,3))
		self.rel.save()

	def tearDown(self):
	    self.artist.delete()
	    self.stage1.delete()
	    self.rel.delete()

	def testStageGet(self):
		response = self.client.get("/api/artists/1/", format="application/json")
		self.assertEqual(response.data['years'],[2014])
		self.assertEqual(response.data['stage_locations'], [1])
		self.assertEqual(len(list(response.data.keys())), 7)
		self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testStageGet2(self):
		response = self.client.get("/api/artists/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/artists/1/", {'artist':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

#/api/artists/year/{year}
class ArtistYearAPITest(APITestCase):
	def setUp(self):

		self.artist = Artist(id=1, name="new artist")
		self.artist.save()
		self.stage1=Stage(location=1)
		self.stage1.save()
		self.rel=stage_artist_yr.create(stage=self.stage1, artist=self.artist, date=datetime.date(2014,2,3))
		self.rel.save()
		self.stage2=Stage(location=2)
		self.stage2.save()
		self.rel2=stage_artist_yr.create(stage=self.stage2, artist=self.artist, date=datetime.date(2013,2,3))
		self.rel2.save()


	def tearDown(self):
	    self.artist.delete()
	    self.stage1.delete()
	    self.stage2.delete()
	    self.rel.delete()
	    self.rel2.delete()

	def testStageGet(self):
	    response = self.client.get("/api/artists/year/2014/", format="application/json")
	    self.assertIsNotNone(response.data)
	    self.assertEqual(response.data[0]['id'],1)
	    self.assertEqual(response.data[0]['stage_location'], 1)
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testStageGet2013(self):
	    response = self.client.get("/api/artists/year/2013/", format="application/json")
	    self.assertIsNotNone(response.data)
	    self.assertEqual(response.data[0]['id'],1)
	    self.assertEqual(response.data[0]['stage_location'], 2)
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testStageGet2(self):
		response = self.client.get("/api/artists/year/2012/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/artists/1/", {'artist':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

#api/artists/
class ArtistsAllAPITest(APITestCase):

    def setUp(self):
        self.a1=Artist(name='2chainz')
        self.a1.save()
        self.a2=Artist(name='miley cyrus')
        self.a2.save()
        self.a3=Artist(name='lady gaga')
        self.a3.save()

    def tearDown(self):
        self.a1.delete()
        self.a2.delete()
        self.a3.delete()

    def testAristAllGet1(self):
        response = self.client.get("/api/artists/", format="application/json")
        self.assertEqual(len(response.data), 3)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

#/api/sponsors/{id}
class SponsorsAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(location=1)
		self.stage.save()
		self.sponsor = Sponsor(id=1, name = "new sponsor")
		self.sponsor.save()
		self.rel=stage_sponsor_yr.create(stage=self.stage, sponsor=self.sponsor, date=datetime.date(2014,1,1))
		self.rel.save()

	def tearDown(self):
	    self.sponsor.delete()
	    self.stage.delete()
	    self.rel.delete()

	def testSponsorGet(self):
		response = self.client.get("/api/sponsors/1/", format="application/json")
		self.assertEqual(response.data['id'],1)
		self.assertEqual(response.data['name'], 'new sponsor')
		self.assertEqual(response.data['years'], [2014])
		self.assertEqual(response.data['stage_locations'],[1])
		self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testSponsorGet2(self):
		response = self.client.get("/api/sponsors/2/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/sponsors/1/", {'sponsor':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

#/api/sponsors/year/{year}
class SponsorYearAPITest(APITestCase):
	def setUp(self):

		self.sponsor = Sponsor(id=1, name="sponsor")
		self.sponsor.save()
		self.stage1=Stage(location=1)
		self.stage1.save()
		self.rel=stage_sponsor_yr.create(stage=self.stage1, sponsor=self.sponsor, date=datetime.date(2014,2,3))
		self.rel.save()
		self.stage2=Stage(location=2)
		self.stage2.save()
		self.rel2=stage_sponsor_yr.create(stage=self.stage2, sponsor=self.sponsor, date=datetime.date(2013,2,3))
		self.rel2.save()

	def tearDown(self):
	    self.sponsor.delete()
	    self.stage1.delete()
	    self.stage2.delete()
	    self.rel.delete()
	    self.rel2.delete()

	def testSponsorGet(self):
	    response = self.client.get("/api/sponsors/year/2014/", format="application/json")
	    self.assertIsNotNone(response.data)
	    self.assertEqual(response.data[0]['id'],1)
	    self.assertEqual(response.data[0]['stage_location'], 1)
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testSponsorGet2013(self):
	    response = self.client.get("/api/sponsors/year/2013/", format="application/json")
	    self.assertIsNotNone(response.data)
	    self.assertEqual(response.data[0]['id'],1)
	    self.assertEqual(response.data[0]['stage_location'], 2)
	    self.assertEqual(status.HTTP_200_OK, response.status_code)

	def testSponsorGet2(self):
		response = self.client.get("/api/sponsors/year/2012/", format="application/json")
		self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

	def testPost(self):
		response = self.client.post("/api/sponsors/1/", {'sponsor':1})
		self.assertEqual(status.HTTP_405_METHOD_NOT_ALLOWED, response.status_code)

#/api/sonsors/
class SponsorsAllAPITest(APITestCase):

    def setUp(self):
        self.a1=Sponsor(name='2chainz')
        self.a1.save()
        self.a2=Sponsor(name='miley cyrus')
        self.a2.save()
        self.a3=Sponsor(name='lady gaga')
        self.a3.save()

    def tearDown(self):
        self.a1.delete()
        self.a2.delete()
        self.a3.delete()

    def testSponsorAllGet1(self):
        response = self.client.get("/api/sponsors/", format="application/json")
        self.assertEqual(len(response.data), 3)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class StageMediaAPITest(APITestCase):

	def setUp(self):
		self.stage = Stage(location=1)
		self.stage.save()
		self.stage_media = StageMedia(year=datetime.date(2014,1,1), bio="stage bio", stage=self.stage)
		self.stage_media.save()
		self.stage_media2 = StageMedia(year=datetime.date(2013,2,3),  bio="stage bio", stage=self.stage)
		self.stage_media2.save()
		self.url1 = "/api/stages/1/media/2014/"
		self.url2 = "/api/stages/1/media/2013/"
		self.bad_url = "/api/stages/2/media/2014/"
		self.data = {"bio": "new stage bio", "location":1}

	def tearDown(self):
		self.stage_media.delete()
		self.stage_media2.delete()
		self.stage.delete()

	def test_stage_media_get1(self):
	    response = self.client.get(self.url1)
	    self.assertEqual(response.data['year'], 2014)
	    self.assertEqual(response.data['location'], 1)
	    self.assertEqual(response.status_code, status.HTTP_200_OK)
	def test_stage_media_get2(self):
	    response = self.client.get(self.url2)
	    self.assertEqual(response.data['year'], 2013)
	    self.assertEqual(response.data['location'], 1)
	    self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_stage_media_bad_get(self):
		response = self.client.get(self.bad_url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_stage_media_post(self):
		response = self.client.post(self.url1, self.data)
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#TODO
class StageMediaListAPITest(APITestCase):

	def setUp(self):
		self.stage = Stage(location=1)
		self.stage.save()
		self.stage_media = StageMedia(year=datetime.date(2014,1,1), bio="stage bio", stage=self.stage)
		self.stage_media.save()
		self.stage_media2 = StageMedia(year=datetime.date(2013,2,2), bio="stage bio", stage=self.stage)
		self.stage_media2.save()
		self.url = "/api/stages/1/media/"
		self.bad_url = "/api/stages/2/media/"
		self.data = {"bio": "new stage bio", "location":1}

	def tearDown(self):
		self.stage_media.delete()
		self.stage_media2.delete()
		self.stage.delete()

	def test_stage_media_get(self):
	    response = self.client.get(self.url)
	    self.assertEqual(len(response.data),2)
	    self.assertEqual(response.data[1]['location'],1)
	    self.assertEqual(response.data[0]['location'], 1)
	    self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_stage_media_bad_get(self):
		response = self.client.get(self.bad_url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_stage_media_post(self):
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class ArtistMediaAPITest(APITestCase):
	def setUp(self):
		self.stage = Stage(location=1)
		self.stage.save()
		self.artist = Artist(id=1, name="new artist")
		self.artist.save()
		self.artist_media = ArtistMedia(bio="artist bio", artist=self.artist)
		self.artist_media.save()
		self.url = "/api/artists/1/media/"
		self.bad_url = "/api/artists/2/media/"
		self.data = {"bio": "new artist bio", "artist":1}

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
		self.sponsor = Sponsor(id=1, name="new sponsor")
		self.sponsor.save()
		self.sponsor_media = SponsorMedia(bio="sponsor bio", sponsor=self.sponsor)
		self.sponsor_media.save()
		self.url = "/api/sponsors/1/media/"
		self.bad_url = "/api/sponsors/2/media/"
		self.data = {"bio": "new sponsor bio", "sponsor":1}

	def tearDown(self):
		self.sponsor_media.delete()
		self.sponsor.delete()

	def test_sponsor_media_get(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_sponsor_media_bad_get(self):
		response = self.client.get(self.bad_url)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

	def test_sponsor_media_post(self):
		response = self.client.post(self.url, self.data)
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
