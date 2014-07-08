from django.test import TestCase
from django.db.utils import IntegrityError

# Create your tests here.

from cs373.models import Artist, Stage, Sponsor

class DjangoMethodTests(TestCase):

    def test_create_artist(self):
        s = Stage(name='Honda')
        s.save()
        a = Artist(name='test',label='test label',origin='austin tx',
                website='cs.utexas.edu',genre='cs',stage=s)
        self.assertIsNotNone(a)

    def test_empty_artist(self):
        s = Stage()
        a = Artist()
        self.assertIsNotNone(a)
        self.assertIsNotNone(s)

    def test_artist(self):
        s = 's'*401
        try:
            a = Artist(name=s,label='test label',origin='austin tx',
                website='cs.utexas.edu',genre='cs')
            a.save()

        except IntegrityError :
            pass

        else:
            self.fail("IntegrityError exception not raised and try block failed")

    def test_sponsor(self):
        s = 's'*401
        try:
            a = Sponsor(name=s)
            a.save()
            #assert(len(a.name) == 401 )

        except IntegrityError :
            pass

        else:
            print("FIXME: max_length should throw exception")
            self.fail("IntegrityError exception not raised or try block failed")

    def test_stage(self):
        s = 's'*401
        try:
            a = Stage(name=s)
            a.save()

        except IntegrityError :
            pass

        else:
            print("FIXME: max_length should throw exception")
            self.fail("IntegrityError exception not raised and try block failed")


    def test_get_artist(self):
        a = Artist()
        self.assertIsNotNone(a)
        self.assertIsNone(a.get_url())

    def test_get_stage(self):
        s = Stage()
        self.assertIsNotNone(s)

    def test_get_sponsor(self):
        s = Sponsor()
        self.assertIsNotNone(s)
