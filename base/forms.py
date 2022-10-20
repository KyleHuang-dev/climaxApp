from django.forms import ModelForm
from .models import Climax


class ClimaxForm(ModelForm):
    class Meta:
        model = Climax
        fields = '__all__'