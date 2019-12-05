from django.db import models

from django.utils.translation import gettext as _

class Squirrel(models.Model):
    
    Longitude = models.FloatField(
    )

    Latitude = models.FloatField(
    )   
    
    Unique_Squirrel_ID = models.CharField(
    max_length=100, 
    )
    
    PM='PM'
    AM='AM'

    Shift_CHOICES=( (PM,'PM'),
    (AM,'AM'),
     )

    Shift = models.CharField(
    max_length=2,
    choices=Shift_CHOICES,
    )


    Date = models.DateField(
    )

    Adult='Adult'
    Juvenile='Juvenile'
    Other='Other'

    Age_CHOICES=( (Adult,'Adult'), 
    (Juvenile,'Juvenile'),
    (Other,'Other')
     )  

    Age = models.CharField( 
    max_length=20, 
    choices=Age_CHOICES,  
    default=Other,
    )

    Gray='Gray'
    Cinnamon='Cinnamon'
    Black='Black'
    Other='Other'

    Primary_Fur_Color_CHOICES=( (Gray,'Gray'),
    (Cinnamon,'Cinnamon'),
    (Black,'Black'),
    (Other,'Other')
    )

    Primary_Fur_Color = models.CharField(
    max_length=100,
    choices=Primary_Fur_Color_CHOICES,
    default=Other,
    )

    Ground_Plane='Ground_Plane'
    Above_Ground='Above_Ground'
    Other='Other'

    Location_CHOICES=( (Ground_Plane,'Ground_Plane'), 
    (Above_Ground,'Above_Ground'),
    (Other,'Other')
     )  

    Location = models.CharField( 
    max_length=100, 
    choices=Location_CHOICES,  
    default=Other,
    )

    Specific_Location= models.CharField(
    max_length=100,
    )
    
    Running = models.NullBooleanField()

    Chasing = models.NullBooleanField()

    Climbing = models.NullBooleanField()

    Eating = models.NullBooleanField()
    
    Foraging = models.NullBooleanField()

    Other_Activities = models.CharField(
            max_length=100,
            )

    Kuks = models.NullBooleanField()

    Quaas = models.NullBooleanField()

    Moans = models.NullBooleanField()

    Tail_flags = models.NullBooleanField()

    Tail_twitches = models.NullBooleanField()

    Approaches = models.NullBooleanField()

    Indifferent= models.NullBooleanField()

    Runs_from = models.NullBooleanField()
    
    def __str__(self):
        return self.Unique_Squirrel_ID
