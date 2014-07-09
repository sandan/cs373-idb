from django.test import TestCase
from django.db.utils import IntegrityError

# Create your tests here.

from cs373.models import Artist, Stage, Sponsor, Member, Photo

class DjangoMethodTests(TestCase):

    # Stage Tests

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
            self.fail('Should have thrown an Exception')
        except:
            pass

    def test_stage_url_1(self):
        s = Stage(name='Stage Name')
        s.save()
        self.assertEqual(s.get_url(),'/stages/1/')

    def test_stage_url_2(self):
        s = Stage(name='Stage One')
        s.save()
        s = Stage(name='Stage Two')
        s.save()
        self.assertEqual(s.get_url(),'/stages/2/')

    def test_stage_url_3(self):
        s = Stage(name='Stage One')
        s.save()
        s = Stage(name='Stage Two')
        s.save()
        s = Stage(name='Stage Three')
        s.save()
        s = Stage.objects.get(pk=2)
        self.assertEqual(s.get_url(),'/stages/2/')

    # Artist Tests

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

    def test_artist_name(self):
        n = 's'*401
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        a = Artist(stage=s)

        try :
            a.save()
            self.fail('Should have thrown an Exception')
        except :
            pass

    def test_artist_url_1(self):
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        a = Artist(stage=s)
        a.save()
        self.assertEqual(a.get_url(),'/artists/1/')

    def test_artist_url_2(self):
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        a = Artist(name='Artist One',stage=s)
        a.save()

        a = Artist(name='Artist Two',stage=s)
        a.save()

        a = Artist(name='Artist Three',stage=s)
        a.save()
        self.assertEqual(a.get_url(),'/artists/3/')

    def test_artist_url_3(self):
        # setup stage
        s = Stage(name='Stage Name')
        s.save()

        a = Artist(name='Artist One',stage=s)
        a.save()

        a = Artist(name='Artist Two',stage=s)
        a.save()

        a = Artist(name='Artist Three',stage=s)
        a.save()

        a = Artist.objects.get(pk=1)
        self.assertEqual(a.get_url(),'/artists/1/')

    # Sponsor Tests

    def test_empty_sponsor(self):
        s = Sponsor()
        s.save()
        s = Sponsor.objects.get(pk=1)
        self.assertIsNotNone(s)
        self.assertEqual(s.name,'')
        self.assertIsNone(s.stage)

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

    def test_sponsor_url_1(self):
        s = Sponsor(name='Sponsor One')
        s.save()

        s = Sponsor(name='Sponsor Two')
        s.save()

        s = Sponsor(name='Sponsor Three')
        s.save()

        self.assertEqual(s.get_url(),'/sponsors/3/')
        self.assertEqual(s.name,'Sponsor Three')

    def test_sponsor_url_2(self):
        s = Sponsor(name='Sponsor One')
        s.save()

        s = Sponsor(name='Sponsor Two')
        s.save()

        s = Sponsor(name='Sponsor Three')
        s.save()

        s = Sponsor.objects.get(pk=1)
        self.assertEqual(s.get_url(),'/sponsors/1/')
        self.assertEqual(s.name,'Sponsor One')

    # Member Tests

    def test_empty_member(self):
        s = Stage(name='Stage One')
        a = Artist(name='Artist One',stage=s)
        m = Member(artist=a)
        self.assertIsNotNone(m)
        self.assertEqual(m.first_name,'')
        self.assertEqual(m.artist,a)

    def test_get_empty_member(self):
        s = Stage(name='Stage One')
        s.save()
        a = Artist(name='Artist One',stage=s)
        a.save()
        m = Member(artist=a)
        m.save()
        self.assertIsNotNone(m)
        self.assertEqual(m.first_name,'')
        self.assertEqual(m.artist,a)

    def test_create_member(self):
        s = Stage(name='Stage One')
        s.save()
        a = Artist(name='Artist One',stage=s)
        a.save()
        m = Member(artist=a,first_name='First',last_name='Last')
        self.assertEqual(m.first_name,'First')
        self.assertEqual(m.last_name,'Last')
        self.assertEqual(m.artist,a)

    def test_get_member(self):
        s = Stage(name='Stage One')
        s.save()
        a = Artist(name='Artist One',stage=s)
        a.save()
        m = Member(artist=a,first_name='First',last_name='Last')
        m.save()

        m = Member.objects.get(pk=1)

        self.assertEqual(m.first_name,'First')
        self.assertEqual(m.last_name,'Last')
        self.assertEqual(m.artist,a)

    def test_str_member(self):
        s = Stage(name='Stage One')
        s.save()
        a = Artist(name='Artist One',stage=s)
        a.save()
        m = Member(artist=a,first_name='First',last_name='Last')
        m.save()

        m = Member.objects.get(pk=1)

        self.assertEqual(m.__str__(),'First Last')

        self.assertEqual(m.first_name,'First')
        self.assertEqual(m.last_name,'Last')
        self.assertEqual(m.artist,a)

    # Photo Tests

    def test_empty_photo(self):
        s = Stage()
        s.save()
        a = Artist(stage=s)
        a.save()
        p = Photo(artist=a)
        p.save()
        self.assertIsNotNone(p)
        self.assertEqual(p.file_name,'')
        self.assertEqual(p.artist,a)

    def test_create_photo(self):
        s = Stage()
        s.save()
        a = Artist(stage=s)
        a.save()
        p = Photo(file_name='/media/1.jpg',artist=a)
        p.save()
        self.assertIsNotNone(p)
        self.assertEqual(p.file_name,'/media/1.jpg')
        self.assertEqual(p.artist,a)


    def test_get_photo(self):
        s = Stage()
        s.save()
        a = Artist(stage=s)
        a.save()
        p = Photo(file_name='/media/1.jpg',artist=a)
        p.save()
        p = Photo(file_name='/media/2.jpg',artist=a)
        p.save()
        p = Photo(file_name='/media/3.jpg',artist=a)
        p.save()

        p = Photo.objects.get(pk=1)

        self.assertIsNotNone(p)
        self.assertEqual(p.file_name,'/media/1.jpg')
        self.assertEqual(p.artist,a)

    def test_str_photo(self):
        s = Stage()
        s.save()
        a = Artist(stage=s)
        a.save()
        p = Photo(file_name='/media/1.jpg',artist=a)
        p.save()
        p = Photo(file_name='/media/2.jpg',artist=a)
        p.save()
        p = Photo(file_name='/media/3.jpg',artist=a)
        p.save()

        p = Photo.objects.get(pk=1)
        self.assertEqual(p.__str__(),'/media/1.jpg')
        p = Photo.objects.get(pk=2)
        self.assertEqual(p.__str__(),'/media/2.jpg')
        p = Photo.objects.get(pk=3)
        self.assertEqual(p.__str__(),'/media/3.jpg')

