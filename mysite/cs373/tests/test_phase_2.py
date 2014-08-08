from django.test import TestCase
from django.db.utils import IntegrityError

# Create your tests here.

from cs373.models import Artist, Stage, Sponsor, Media, ArtistMedia, SponsorMedia, StageMedia

class DjangoMethodTests(TestCase):

    # Stage Tests

    def test_create_empty_stage(self):
        s = Stage()
        self.assertIsNotNone(s)
        self.assertEqual(s.location,None)

    def test_create_stage(self):
        s = Stage(location=1)
        self.assertIsNotNone(s)
        self.assertEqual(s.location,1)

    def test_get_stage(self):
        s = Stage(location=2)
        s.save()
        b = Stage.objects.get(location=2)
        self.assertIsNotNone(b)
        self.assertEqual(b.location,2)
        self.assertEqual(b,s)

    def test_stage_location(self):
        n = 9999999999999999999
        s = Stage(location=n)
        try:
            s.save()
            self.fail('Should have thrown an Exception')
        except:
            pass

    # Artist Tests

    def test_create_artist(self):
        # test artist
        a = Artist(name='Artist Name',label='Artist Label',origin='Artist City',genre='Artist Genre')
        self.assertIsNotNone(a)
        self.assertEqual(a.name,'Artist Name')
        self.assertEqual(a.label,'Artist Label')
        self.assertEqual(a.origin,'Artist City')
        self.assertEqual(a.genre,'Artist Genre')

    def test_get_artist(self):

        # test artist
        a = Artist(name='Artist Name',label='Artist Label',origin='Artist City',genre='Artist Genre')
        a.save()
        b = Artist.objects.get(name='Artist Name')
        self.assertIsNotNone(b)
        self.assertEqual(b.name,'Artist Name')
        self.assertEqual(b.label,'Artist Label')
        self.assertEqual(b.origin,'Artist City')
        self.assertEqual(b.genre,'Artist Genre')


    def test_artist_url_1(self):

        a = Artist()
        a.save()
        self.assertEqual(a.get_absolute_url(),'/artists/{:d}/'.format(a.id))


    def test_artist_url_2(self):
        a = Artist(id=1,name='Artist One')
        a.save()

        a = Artist(id=2,name='Artist Two')
        a.save()

        a = Artist(id=3,name='Artist Three')
        a.save()
        self.assertEqual(a.get_absolute_url(),'/artists/{:d}/'.format(a.id))

    def test_artist_url_3(self):
        a = Artist(id=1, name='Artist One')
        a.save()

        a = Artist(id=2, name='Artist Two')
        a.save()

        a = Artist(id=3, name='Artist Three')
        a.save()

        a = Artist.objects.get(name='Artist One')
        self.assertEqual(a.get_absolute_url(),'/artists/{:d}/'.format(a.id))

    # Sponsor Tests

    def test_empty_sponsor(self):
        s = Sponsor()
        s.save()
        self.assertIsNotNone(s)


    def test_save_sponsor(self):
        s = Sponsor(name='Sponsor Name')
        s.save()
        z = Sponsor.objects.get(name='Sponsor Name')
        self.assertIsNotNone(z)
        self.assertEqual(s, z)

    def test_sponsor_name(self):
        n = 'n'*401
        s = Sponsor(name=n)
        try:
            s.save()
            self.fail('Should have thrown an exception')
        except:
            pass

    def test_get_sponsor_name(self):
        s = Sponsor(name='Sponsor Name')
        s.save()
        s = Sponsor.objects.get(name='Sponsor Name')
        self.assertIsNotNone(s)
        self.assertEqual(s.__str__(),'Sponsor Name')

    def test_get_sponsor(self):

        # test artist
        a = Sponsor(name='sponsor', industry='business')
        a.save()
        b = Sponsor.objects.get(name='sponsor')
        self.assertIsNotNone(b)
        self.assertEqual(b.name,'sponsor')
        self.assertEqual(b.industry,'business')


    def test_sponsor_url_1(self):
        s = Sponsor(id=1, name='Sponsor One')
        s.save()

        s = Sponsor(id=2, name='Sponsor Two')
        s.save()

        s = Sponsor(id=3, name='Sponsor Three')
        s.save()

        self.assertEqual(s.get_absolute_url(),'/sponsors/{:d}/'.format(s.id))
        self.assertEqual(s.name,'Sponsor Three')

    def test_sponsor_url_2(self):
        s = Sponsor(id=1, name='Sponsor One')
        s.save()

        s = Sponsor(id=2, name='Sponsor Two')
        s.save()

        s = Sponsor(id=3, name='Sponsor Three')
        s.save()

        s = Sponsor.objects.get(name='Sponsor Two')
        self.assertEqual(s.get_absolute_url(),'/sponsors/{:d}/'.format(s.id))
        self.assertEqual(s.name,'Sponsor Two')

    def test_sponsor_url_3(self):
        s = Sponsor(id=1, name='Sponsor One')
        s.save()

        s = Sponsor(id=2, name='Sponsor Two')
        s.save()

        s = Sponsor(id=3, name='Sponsor Three')
        s.save()

        s = Sponsor.objects.get(name='Sponsor One')
        self.assertEqual(s.get_absolute_url(),'/sponsors/{:d}/'.format(s.id))
        self.assertEqual(s.name,'Sponsor One')

    # Media tests

    def test_empty_media(self):

        a = Artist(name='z')
        a.save()
        m = ArtistMedia(artist=a)
        try:
            m.save()
            self.fail('Should have thrown an Exception')
        except:
            pass

    def test_save_media(self):

        a = Artist(name='z')
        a.save()
        m = ArtistMedia(artist=a)
        m.save()

        m = ArtistMedia.objects.get(artist=a)
        self.assertIsNotNone(m)
        self.assertEqual(m.artist,a)

    def test_media_length(self):
        n = 'm'*256
        self.assertEqual(len(n),256)

        m = ArtistMedia(bio=n)
        try:
            m.save()
            self.fail('Should have thrown an Exception')
        except:
            pass

    def test_media_string(self):

        a = Artist(name='z')
        a.save()
        m = ArtistMedia(artist=a, webpage='www.www.com')
        m.save()
        self.assertEqual(super(ArtistMedia,m).__str__(), 'www.www.com')



