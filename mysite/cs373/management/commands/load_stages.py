from django.core.management.base import BaseCommand,CommandError
from cs373.models import StageMedia, Stage

#see load_sponsors
class Command(BaseCommand):

    def handle(self, *args, **options):
        for path in args:
            if ('stage' not in path):
                raise CommandError("Make sure the file has 'stage' in the name")
            else:
                self.load(path)


    def load(self,p):
        with open(p) as f:
            F=iter(f)
            stage_dict=dict()
            stage_media_dict=dict()
            current_stage=None
            y = line.split(': ')
            d = y[2].split(', ')
            
            year = d[0]
            month = d[1]
            day = d[2]
            
            date = datetime.date(year,month,day)
            
            for line in F:
                if (line == "\n"):
                    #new stage+media
                    current_stage=create_stage(stage_dict)
                    stage_dict.clear()
                    self.create_stage_media(stage_media_dict,current_stage, date)
                    stage_media_dict.clear()

                else:
                    info=line.split(': ')
                    assert (len(info)==2)
                    key=info[0].lower()
                    val=info[1].strip()
                    
                    if (key == 'location'):
                        stage_dict[key]=val
                    
                    else:
                        stage_media_dict[key]=val


    def create_stage(self, data):

        s=Stage(**data)
        s.save()
        self.stdout.write("+created: stage: "+data['name'])
        return s

    def create_stage_media(self, stage_data, stage, date):

        sm=StageMedia(**stage_data)
        sm.stage=stage
        sm.year = date
        sm.save()
        self.stdout.write("+created: "+ stage.name)
