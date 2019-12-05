from .models import Squirrel
from django.forms import ModelForm
class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'
