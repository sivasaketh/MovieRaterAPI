from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating

# Create your views here.
class MovieViewset(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            print(movie.movie)
            response = {'message': 'It worked'}
            return Response(response, status = status.HTTP_200_OK)
        else:
            response = {'message': 'Provide stars'}
            return Response(response, status = status.HTTP_400_BAD_REQUEST)

class RatingViewset(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Rating.objects.all()