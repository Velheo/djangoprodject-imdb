from django.forms import ModelForm
from .models import *

class MovieModelForm(ModelForm):
    class Meta:
        model=Movie
        fields='__all__'

#class DirectorModelForm(ModelForm):
#    class Meta:
#        model=Director
#        fields='__all__'