from django.forms import ModelForm
from .models import DeicideList

class DeicideListForm(ModelForm):
    class Meta:
        model = DeicideList
        fields = ['Gods_Name', 'Accusation']
