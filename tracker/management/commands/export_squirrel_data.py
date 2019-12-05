class Command(BaseCommand):
    help = 'Export squirrel data to a csv file, save it in designated path'
    
    def add_arguments(self, parser):
        parser.add_argument('path')
    
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        fields = Squirrel._meta.fields
        with open(path, 'w') as data_file:
            writer = csv.writer(data_file)
            for object in Squirrel.objects.all():
                row = []
                for field in fields:
                    row.append(getattr(object, field.name))
                writer.writerow(row)

