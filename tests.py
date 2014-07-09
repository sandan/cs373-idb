from django.test import TestCase
from django.db.utils import IntegrityError

# Create your tests here.

from cs373.models import Artist, Stage, Sponsor

class DjangoMethodTests(TestCase):

    def test_create_empty_stage(self):
        s = Stage()
        self.assertIsNotNone(s)
        self.assertEqual(s.name,'')

    def test_create_stage(self):
        s = Stage(name='Stage Name')
        self.assertIsNotNone(s)
        self.assertEqual(s.name,'Stage Name')

    def test_get_stage(self):
        s = Stage(name='Stage Name')
        s.save()
        b = Stage.objects.get(pk=1)
        self.assertIsNotNone(b)
        self.assertEqual(b.name,'Stage Name')
        self.assertEqual(b,s)

    def test_stage_name(self):
        n = 's'*401
        self.assertEqual(len(n),401)

        s = Stage(name=n)
        try:
            s.save()
            self.fail('Should have thrown an error')
        except:
            pass


    def test_create_artist(self):
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        # test artist
        a = Artist(name='Artist Name',label='Artist Label',origin='Artist City',website='http://www.artist.com/',genre='Artist Genre',stage=s)
        self.assertIsNotNone(a)
        self.assertEqual(a.name,'Artist Name')
        self.assertEqual(a.label,'Artist Label')
        self.assertEqual(a.origin,'Artist City')
        self.assertEqual(a.website,'http://www.artist.com/')
        self.assertEqual(a.genre,'Artist Genre')
        self.assertEqual(a.stage,s)


    def test_get_artist(self):
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        # test artist
        a = Artist(name='Artist Name',label='Artist Label',origin='Artist City',website='http://www.artist.com/',genre='Artist Genre',stage=s)
        a.save()
        b = Artist.objects.get(name='Artist Name')
        self.assertIsNotNone(b)
        self.assertEqual(b.name,'Artist Name')
        self.assertEqual(b.label,'Artist Label')
        self.assertEqual(b.origin,'Artist City')
        self.assertEqual(b.website,'http://www.artist.com/')
        self.assertEqual(b.genre,'Artist Genre')
        self.assertEqual(b.stage,s)

    def test_empty_artist(self):
        a = Artist()
        try:
            a.save()
            self.fail('Should have thrown IntegrityError')
        except IntegrityError:
            pass

    def test_empty_artist_with_stage(self):
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        a = Artist(stage=s)
        a.save()
        a = Artist.objects.get(pk=1)
        self.assertIsNotNone(a)
        self.assertEqual(a.name,'')
        self.assertEqual(a.label,'')
        self.assertEqual(a.origin,'')
        self.assertEqual(a.website,'')
        self.assertEqual(a.genre,'')
        self.assertEqual(a.stage,s)

    def test_empty_sponsor(self):
        s = Sponsor()
        s.save()
        s = Sponsor.objects.get(pk=1)
        self.assertIsNotNone(s)
        self.assertEqual(s.name,'')

    def test_save_sponsor(self):
        s = Sponsor(name='Sponsor Name')
        s.save()
        s = Sponsor.objects.get(pk=1)
        self.assertIsNotNone(s)
        self.assertEqual(s.name,'Sponsor Name')

    def test_get_sponsor_name(self):
        s = Sponsor(name='Sponsor Name')
        s.save()
        s = Sponsor.objects.get(pk=1)
        self.assertIsNotNone(s)
        self.assertEqual(s.__str__(),'Sponsor Name')

    # def test_create_artist(self):
    #     s = Stage(name='Honda')
    #     s.save()
    #     a = Artist(name='test',label='test label',origin='austin tx',
    #             website='cs.utexas.edu',genre='cs',stage=s)
    #     self.assertIsNotNone(a)

    # def test_empty_artist(self):
    #     s = Stage()
    #     a = Artist()
    #     self.assertIsNotNone(a)
    #     self.assertIsNotNone(s)

    # def test_artist(self):
    #     s = 's'*401
    #     try:
    #         a = Artist(name=s,label='test label',origin='austin tx',
    #             website='cs.utexas.edu',genre='cs')
    #         a.save()

    #     except IntegrityError :
    #         pass

    #     else:
    #         self.fail("IntegrityError exception not raised and try block failed")

    # def test_sponsor(self):
    #     s = 's'*401
    #     try:
    #         a = Sponsor(name=s)
    #         a.save()
    #         #assert(len(a.name) == 401 )

    #     except IntegrityError :
    #         pass

    #     else:
    #         print("FIXME: max_length should throw exception")
    #         self.fail("IntegrityError exception not raised or try block failed")
