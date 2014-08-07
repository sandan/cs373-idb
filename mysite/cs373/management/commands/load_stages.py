from django.core.management.base import BaseCommand,CommandError
from cs373.models import StageMedia, Stage
from datetime import date

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
            festDate = None

            for line in F:
                if (line == "\n"):
                    #new stage+media
                    current_stage = self.get_or_create(stage_dict)
                    stage_dict.clear()
                    self.create_stage_media(stage_media_dict, current_stage, festDate)
                    stage_media_dict.clear()

                else:
                    info=line.split(': ')
                    assert (len(info)==2)
                    key=info[0].lower()
                    val=info[1].strip()

                    if (key == 'year'):
                        d = val.split(',')
                        year = int(d[0])
                        month = int(d[1])
                        day = int(d[2])
                        festDate = date(year, month, day)

                    elif (key == 'location'):
                        stage_dict[key]=val

                    else:
                        if (val.lower()!='null'):
                            stage_media_dict[key]=val


    def get_or_create(self, data):
        try:
            l=data['location']
            s=Stage.objects.get(location=l)
            return s

        except Exception:
            return self.create_stage(data)

    def create_stage(self, data):

        s=Stage(**data)
        s.save()
        self.stdout.write("+created: stage: "+data['location'])
        return s

    def create_stage_media(self, stage_data, stage, festDate):

        sm = StageMedia(**stage_data)
        sm.stage = stage
        sm.year = festDate
        sm.save()
        self.stdout.write("+created: stageMedia: "+ sm.name)