from django.core.management.base import BaseCommand,CommandError
from cs373.models import ArtistMedia, Artist, Stage

#see load_sponsors
class Command(BaseCommand):

    def handle(self, *args, **options):
        for path in args:

            if ('artist' not in path):
                raise CommandError("Make sure the file has 'artist' in the name")

            else:
                self.load(path)

    def load(self,p):
        with open(p) as f:
            F=iter(f)
            artist_dict=dict()
            artist_media_dict=dict()
            current_artist=None
            for line in F:
                if (line == "\n"):
                    #new artist+media
                    
                    current_artist = self.create_artist(artist_dict)
                    artist_dict.clear()
                    self.create_artist_media(artist_media_dict,current_artist)
                    artist_media_dict.clear()

                else:

                    info=line.split(': ')
                    assert (len(info)==2)
                    key=info[0].lower()
                    val=info[1].strip()


                    if (key == 'name' or key=='label' or key== 'origin' or key=='genre' ):
                        artist_dict[key]=val

                    else:
                        artist_media_dict[key]=val



    def create_artist(self, artist_data):
        a=Artist(**artist_data)
        a.save()
        self.stdout.write("+created artist: "+artist_data['name'])
        return a

    def create_artist_media(self, data, artist):
        am=ArtistMedia(**data)
        am.artist = artist
        am.save()

        self.stdout.write("+created media for: "+ artist.name)
