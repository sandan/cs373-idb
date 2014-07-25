from django.core.management.base import BaseCommand,CommandError
from cs373.models import SponsorMedia, Sponsor, Stage
"""
Make sure the format is as follows  (where attribute follows from the model):
[attribute: value
attribute: value
.
.
.
attribute: value ] for 1 entry

[attribute: value
attribute: value
.
.
.
attribute: value ] for another entry, also make sure there is a newline at the end of the file
so that there is an empty line separating the last block and the EOF

"""
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
                    sponsor_dict.clear()
                    self.create_sponsor_media(sponsor_media_dict,current_sponsor)

                else:

                    info=line.split(': ')
                    assert (len(info)==2)
                    key=info[0].lower()
                    val=info[1].strip()


                    if (key == 'name' or key=='business_type'):
                        sponsor_dict[key]=val

                    elif (key== 'stage'):
                        s=Stage.objects.get(name=val)
                        current_sponsor=self.create_sponsor(sponsor_dict,s)

                    else:
                        sponsor_media_dict[key]=val



    def create_sponsor(self, sponsor_data, stage):
        a=Sponsor(**sponsor_data)
        a.stage=stage
        stage.save()
        a.save()
        self.stdout.write("+created sponsor: "+sponsor_data['name'])
        return a

    def create_sponsor_media(self, data, sponsor):
        sm=SponsorMedia(**data)
        sponsor.save()
        sm.sp=sponsor
        sm.save()

        self.stdout.write("+created media for: "+ sponsor.name)