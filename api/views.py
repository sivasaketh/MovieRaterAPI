from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating

# Create your views here.
class MovieViewset(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' and 'movie' in request.data:
            movie = Movie.objects.get(id=pk)
            user = User.objects.get(id=1)
            stars = request.data['stars']

            try:
                rating = Rating.objects.get(movie=movie, user=user)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result':serializer.data}
                return Response(response, status = status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(movie=movie, user=user, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result':serializer.data}
                return Response(response, status = status.HTTP_200_OK)
        else:
            response = {'message': 'Provide stars'}
            return Response(response, status = status.HTTP_400_BAD_REQUEST)

class RatingViewset(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()