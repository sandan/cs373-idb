from django.test import TestCase
from cs373.models import *
from django.db.utils import IntegrityError
import datetime


class TypeTest(TestCase):

    #test the types of models created
    def test_types(self):
        a=Artist()
        s=Stage()
        p=Sponsor()

        self.assertEqual(type(a), Artist)
        self.assertEqual(type(p), Sponsor)
        self.assertEqual(type(s), Stage)

    #test types of relationship classes
    def test_types_relationships1(self):
        a=Artist()
        s=Stage()
        p=Sponsor()

        #correct artist type but not correct stage type
        try:
            stage_artist_yr.create(stage=p,artist=a,date=datetime.date(1999,3,3))
        except AssertionError:
            pass
        except Exception:
            self.fail("Unknown exception thrown!")
        else:
            self.fail("Expected exception to be thrown but it wasn't !")

        #correct stage type but not correct artist type
        try:
            stage_artist_yr.create(stage=s,artist=p,date=datetime.date(1999,3,3))
        except AssertionError:
            pass
        except Exception:
            self.fail("Unknown exception thrown!")
        else:
            self.fail("Expected exception to be thrown but it wasn't !")

        #both wrong types
        try:
            stage_artist_yr.create(stage=p,artist=a,date=datetime.date(1999,3,3))
        except AssertionError:
            pass
        except Exception:
            self.fail("Unknown exception thrown!")
        else:
            self.fail("Expected exception to be thrown but it wasn't !")

    def test_types_relationships2(self):
        a=Artist()
        s=Stage()
        p=Sponsor()

        try:
            stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2100,3,3))
        except AssertionError:
            pass
        except Exception:
            self.fail("Unknown exception thrown!")
        else:
            self.fail("Expected exception to be thrown but it wasn't !")

        try:
            stage_sponsor_yr.create(stage=a,sponsor=p,date=datetime.date(1999,3,3))
        except AssertionError:
            pass
        except Exception:
            self.fail("Unknown exception thrown!")
        else:
            self.fail("Expected exception to be thrown but it wasn't !")

        try:
            stage_sponsor_yr.create(stage=a,sponsor=s,date=datetime.date(1999,3,3))
        except AssertionError:
            pass
        except Exception:
            self.fail("Unknown exception thrown!")
        else:
            self.fail("Expected exception to be thrown but it wasn't !")

class StageRelationshipTests(TestCase):

    #test creation and insertion
    def test_relationship1(self):
        s=Stage(location=2)
        s.save()

        a=Artist(name="hello")
        a.save()

        rel=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2005,10,2))
        rel.save()

        self.assertEqual(rel.get_yr(),2005)
        self.assertEqual(rel.key,str(a.id)+str(rel.get_yr()))
        self.assertEqual('hello',rel.artist.name)
        self.assertEqual(2,rel.stage.location)


    def test_relationship2(self):
        s=Stage(location=2)
        s.save()

        a=Sponsor(name="hello")
        a.save()

        rel=stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2099,10,2))
        rel.save()

        self.assertEqual(rel.get_yr(),2099)
        self.assertEqual(rel.key,str(a.id)+str(rel.get_yr()))
        self.assertEqual('hello',rel.sponsor.name)
        self.assertEqual(2,rel.stage.location)

class ConstraintTests(TestCase):

    #same artist playing on two different stages of the same year
    def test_constraint_violation1(self):
        s=Stage(location=2)
        t=Stage(location=3)
        s.save()
        t.save()

        a=Artist(name='hello world')
        a.save()

        rel1=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2011,1,1))
        rel1.save()
        try:
            rel2=stage_artist_yr.create(stage=t,artist=a,date=datetime.date(2011,2,3))
            rel2.save()
        except IntegrityError:
            pass
        except Exception:
            self.fail("Unexpected Exception thrown!")
        else:
            self.fail("An exception expected to be thrown but wasn't!")

    #same sponsor sponsoring more than one stage in the same year
    def test_constraint_violation2(self):
        s=Stage(location=2)
        t=Stage(location=3)
        s.save()
        t.save()

        a=Sponsor(name='hello world')
        a.save()

        rel1=stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2099,1,1))
        rel1.save()
        try:
            rel2=stage_sponsor_yr.create(stage=t,sponsor=a,date=datetime.date(2099,2,3))
            rel2.save()
        except IntegrityError:
            pass
        except Exception:
            self.fail("Unexpected Exception thrown!")
        else:
            self.fail("An exception expected to be thrown but wasn't!")

    #should be ok to save relationships on same stage if both are from a different year
    def test_no_constraint_violation1(self):
        s=Stage(location=2)
        t=Stage(location=3)
        s.save()
        t.save()

        a=Artist(name='hello world')
        a.save()

        rel1=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2012,1,1))
        rel1.save()

        rel2=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2011,1,1))
        rel2.save()


    #same deal for sponsors
    def test_no_constraint_violation2(self):
        s=Stage(location=2)
        t=Stage(location=3)
        s.save()
        t.save()

        a=Sponsor(name='hello world')
        a.save()

        rel1=stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2010,1,1))
        rel1.save()

        rel2=stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2011,1,1))
        rel2.save()

class MultiRelationTest(TestCase):

    #test accessing child objects
    def test_access_artist_stage0(self):
        s=Stage(location=1)
        s.save()
        for i in range(10):
            a=Artist(name=str(i))
            a.save()
            rel=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2014,10,10))
            rel.save()

        self.assertEqual(len(s.stage_artist_yr_set.all()),10)

    #test accessing parent object
    def test_access_artist_stage1(self):
        s=Stage(location=1)
        s.save()
        for i in range(10):
            a=Artist(name=str(i))
            a.save()
            rel=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2014,10,10))
            rel.save()

        for a in s.stage_artist_yr_set.all():
            self.assertEqual(a.stage,s)

    #test accessing child objects (same deal as above but with sponsor)
    def test_access_sponsor_stage2(self):
        s=Stage(location=1)
        s.save()
        for i in range(10):
            a=Sponsor(name=str(i))
            a.save()
            rel=stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2034,10,12))
            rel.save()

        self.assertEqual(len(s.stage_sponsor_yr_set.all()),10)

    #test accessing parent object
    def test_access_sponsor_stage3(self):
        s=Stage(location=1)
        s.save()
        for i in range(10):
            a=Sponsor(name=str(i))
            a.save()
            rel=stage_sponsor_yr.create(stage=s,sponsor=a,date=datetime.date(2014,10,10))
            rel.save()

        for a in s.stage_sponsor_yr_set.all():
            self.assertEqual(a.stage,s)

class CrossRelationTest(TestCase):
    """
    Tests retrieving members of a time relationship
    """

    #retrieve stage,sponsor,artist
    def test_cross_rel1(self):
        s=Stage(location=10)
        a=Artist(name="Hello World")
        sp=Sponsor(name="Rich People")

        s.save()
        a.save()
        sp.save()

        rel_artist_stage=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2012,12,25))
        rel_sponsor_stage=stage_sponsor_yr.create(stage=s,sponsor=sp,date=datetime.date(2012,12,25))

        rel_artist_stage.save()
        rel_sponsor_stage.save()

        self.assertEqual(s.stage_artist_yr_set.all()[0],rel_artist_stage)
        self.assertEqual(s.stage_sponsor_yr_set.all()[0],rel_sponsor_stage)

        self.assertEqual(a.stage_artist_yr_set.all()[0],rel_artist_stage)
        self.assertEqual(sp.stage_sponsor_yr_set.all()[0],rel_sponsor_stage)

    #retrieve by relationship
    def test_cross_rel2(self):
        s=Stage(location=10)
        a=Artist(name="Hello World")
        sp=Sponsor(name="Rich People")

        s.save()
        a.save()
        sp.save()

        rel_artist_stage=stage_artist_yr.create(stage=s,artist=a,date=datetime.date(2012,12,25))
        rel_sponsor_stage=stage_sponsor_yr.create(stage=s,sponsor=sp,date=datetime.date(2012,12,25))

        rel_artist_stage.save()
        rel_sponsor_stage.save()

        self.assertEqual(a, rel_artist_stage.artist)
        self.assertEqual(s, rel_artist_stage.stage)

        self.assertEqual(sp, rel_sponsor_stage.sponsor)
        self.assertEqual(s, rel_artist_stage.stage)

class SimulationsTest(TestCase):

    def test_simulation(self):
        #create simulation of the acl festival
        stages=[]
        sponsors=[]
        artists=[]

        #initialize
        for i in range(3):
            x=Stage(location=i)
            y=Artist(name=str(i))
            z=Sponsor(name=str(i))
            x.save()
            y.save()
            z.save()
            stages.append(x)
            artists.append(y)
            sponsors.append(z)

        stage_sponsor=zip(stages,sponsors)
        stage_artist=zip(stages,artists)

        stage_sponsor_rels=list(map(
            lambda elements: stage_sponsor_yr.create(stage=elements[0],sponsor=elements[1],date=datetime.date(2011,3,4)),
            stage_sponsor))
        stage_artist_rels=list(map(
            lambda elements: stage_artist_yr.create(stage=elements[0],artist=elements[1],date=datetime.date(2011,3,4)),
            stage_artist))

        for x,y in zip(stage_sponsor_rels,stage_artist_rels):
            x.save()
            y.save()

        #check that relationships see them
        self.assertEqual(len(list(filter(lambda x: x.stage.location == int(x.sponsor.name), stage_sponsor_rels))), 3)
        self.assertEqual(len(list(filter(lambda x: x.stage.location == int(x.artist.name), stage_artist_rels))), 3)

        self.assertEqual(3, len(stage_artist_yr.objects.all()))
        self.assertEqual(3, len(stage_sponsor_yr.objects.all()))

        #check that they see relationships
        for i in range(3):
            a=Artist.objects.filter(name=str(i))[0]
            for st in a.stage_artist_yr_set.all():
                self.assertEqual(st.stage.location, int(a.name))

            sp=Sponsor.objects.filter(name=str(i))[0]
            for st in sp.stage_sponsor_yr_set.all():
                self.assertEqual(st.stage.location, int(sp.name))

            st=Stage.objects.filter(location=i)[0]
            for ar in st.stage_artist_yr_set.all():
                self.assertEqual(int(ar.artist.name),st.location)

            for s in st.stage_sponsor_yr_set.all():
                self.assertEqual(int(s.sponsor.name),st.location)

        #start adding 2012 info

        #artist1 plays again on stage 1
        m=Artist.objects.filter(name='1')[0]
        sta=Stage.objects.filter(location=1)[0]
        m.stage_artist_yr_set.add(stage_artist_yr.create(stage=sta, artist=m, date=datetime.date(2012,3,4)))

        #but this time with sponsor 2
        n=Sponsor.objects.filter(name='2')[0]
        n.stage_sponsor_yr_set.add(stage_sponsor_yr.create(stage=sta, sponsor=n, date=datetime.date(2012,3,4)))

        #check that relationships is made
        self.assertEqual(len(stage_sponsor_yr.objects.all()),4)

        #artist2 plays on stage 0 with sponsor 1
        m=Artist.objects.filter(name='2')[0]
        sta=Stage.objects.filter(location=0)[0]
        m.stage_artist_yr_set.add(stage_artist_yr.create(stage=sta, artist=m, date=datetime.date(2012,3,4)))
        n=Sponsor.objects.filter(name='1')[0]
        n.stage_sponsor_yr_set.add(stage_sponsor_yr.create(stage=sta, sponsor=n, date=datetime.date(2012,3,4)))






















