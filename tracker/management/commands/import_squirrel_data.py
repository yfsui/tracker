import csv
from django.core.management.base import BaseCommand
from tracker.models import Squirrel

class Command(BaseCommand):
    
    help = 'Pass in a file path to import squirrel data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path')
    
    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        
        with open(options['path']) as data_file:  
            reader = csv.DictReader(data_file)
            data = list(reader)
            for data_object in data:
                Longitude = data_object['X']
                Latitude = data_object['Y']
                Unique_Squirrel_ID = data_object['Unique Squirrel ID']
                Shift = data_object['Shift']
                Date = data_object['Date'][4:]+'-'+ data_object['Date'][:2]+'-'+data_object['Date'][2:4]
                Age = data_object['Age']
                Primary_Fur_Color = data_object['Primary Fur Color']
                Location = data_object['Location']
                Specific_Location = data_object['Specific Location']
                Running = bool(data_object['Running'])
                Chasing = bool(data_object['Chasing'])
                Climbing = bool(data_object['Climbing'])
                Eating = bool(data_object['Eating'])
                Foraging = bool(data_object['Foraging'])
                Other_Activities = data_object['Other Activities']
                Kuks = bool(data_object['Kuks'])
                Quaas = bool(data_object['Quaas'])
                Moans = bool(data_object['Moans'])
                Tail_flags = bool(data_object['Tail flags'])
                Tail_twitches = bool(data_object['Tail twitches'])
                Approaches = bool(data_object['Approaches'])
                Indifferent = bool(data_object['Indifferent'])
                Runs_from = bool(data_object['Runs from'])
                
                squirrel=Squirrel(
                        Longitude = Longitude,
                        Latitude = Latitude,
                        Unique_Squirrel_ID = Unique_Squirrel_ID,
                        Shift = Shift,
                        Date = Date,
                        Age = Age,
                        Primary_Fur_Color = Primary_Fur_Color,
                        Location = Location,
                        Specific_Location = Specific_Location,
                        Running = Running,
                        Chasing = Chasing,
                        Climbing = Climbing,
                        Eating = Eating,
                        Foraging = Foraging,
                        Other_Activities = Other_Activities,
                        Kuks = Kuks,
                        Quaas = Quaas,
                        Moans = Moans,
                        Tail_flags = Tail_flags,
                        Tail_twitches = Tail_twitches,
                        Approaches = Approaches,
                        Indifferent = Indifferent,
                        Runs_from = Runs_from,
                        )
                squirrel.save()
    def bool(string):
        if (string.lower()=='true'):
            return True
        else:
            return False
