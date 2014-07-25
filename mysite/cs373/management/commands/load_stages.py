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
            for line in F:
                if (line == "\n"):
                    #new stage+media
                    stage_dict.clear()
                    self.create_stage_media(stage_media_dict,current_stage)
                    stage_media_dict.clear()

                else:
                    info=line.split(': ')
                    assert (len(info)==2)

                    if (info[0].lower() == 'name'):
                        stage_dict[info[0].lower()]=info[1].strip()
                        current_stage=self.create_stage(stage_dict)

                    else:
                        if (info[1].lower() == 'null\n'):
                            continue
                        stage_media_dict[info[0].lower()]=info[1].strip()


    def create_stage(self, data):

        s=Stage(**data)
        s.save()
        self.stdout.write("+created: stage: "+data['name'])
        return s

    def create_stage_media(self, stage_data, stage):

        sm=StageMedia(**stage_data)
        sm.st=stage
        stage.save()
        sm.save()
        self.stdout.write("+created: "+ stage.name)