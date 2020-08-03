from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie', 'description']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'user', 'movie', 'stars']
