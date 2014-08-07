from django.core.management.base import BaseCommand,CommandError
from cs373.models import *
import datetime

#The stage/media and artist data should already be loaded into the DB at this point
class Command(BaseCommand):

    def handle(self, *args, **options):
        for path in args:
            if ('stage_artist' not in path):
                raise CommandError("Make sure the file has 'stage_artist' in the name")
            else:
                self.load(path)


    def load(self,p):
        with open(p) as f:
            for line in f:
                info=line.split()
                assert len(info) == 3
                self.relate(self.get_stage(info[0]),self.get_artist(info[1].replace('_',' ')),int(info[2]))

    def relate(self, stage, artist, year):
        assert type(stage)==Stage
        assert type(artist) == Artist
        assert type(year) == int
        r=stage_artist_yr.create(stage=stage, artist=artist, date=self.get_stage_date(stage,year))
        r.save()
        self.stdout.write("+created relation on stage: "+str(stage.location)+' with artist: '+artist.name+' for year: '+str(year))

    def get_stage(self, location):
        return Stage.objects.get(location=location)

    def get_artist(self, name):
        return Artist.objects.get(name=name)

    def get_stage_date(self, st, yr):
        m=st.stagemedia_set.filter(year__year=yr)
        if (len(m) == 0 ):
            return datetime.date(yr,10,4) #default date if none given
        else:
            return m[0].year #return the stagemedia date for the festival
