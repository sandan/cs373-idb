from django.core.management.base import BaseCommand,CommandError
from cs373.models import SponsorMedia, Sponsor, Stage

class Command(BaseCommand):

    def handle(self, *args, **options):
        for path in args:
            if ('sponsor' not in path):
                raise CommandError("Make sure the file has 'sponsor' in the name")

            else:
                self.load(path)


    def load(self,p):
        with open(p) as f:
            F=iter(f)
            sponsor_dict=dict()
            sponsor_media_dict=dict()
            current_sponsor=None
            for line in F:
                if (line == "\n"):
                    #new sponsor+media
                    current_sponsor = self.create_sponsor(sponsor_dict)
                    sponsor_dict.clear()
                    self.create_sponsor_media(sponsor_media_dict,current_sponsor)
                    sponsor_media_dict.clear()
                else:

                    info=line.split(': ')
                    assert (len(info)==2)
                    key=info[0].lower()
                    val=info[1].strip()



                    if (key == 'name' or key=='industry'):
                        sponsor_dict[key]=val

                    else:
                        if (val.lower() != 'null'):
                            sponsor_media_dict[key]=val



    def create_sponsor(self, sponsor_data):
        a=Sponsor(**sponsor_data)
        a.save()
        self.stdout.write("+created sponsor: "+sponsor_data['name'])
        return a

    def create_sponsor_media(self, data, sponsor):
        sm=SponsorMedia(**data)
        sm.sponsor=sponsor
        sm.save()

        self.stdout.write("+created media for: "+ sponsor.name)