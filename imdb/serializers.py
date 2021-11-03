from rest_framework import serializers
from .models import *

class MovieSerializer1(serializers.ModelSerializer):
    director=serializers.StringRelatedField()
    class Meta:
        model=Movie
        fields=['title', 'director', 'year', 'rating']
class MovieSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id', 'title']