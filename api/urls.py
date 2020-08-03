from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewset, RatingViewset

router = routers.DefaultRouter()
router.register('movies', MovieViewset)
router.register('ratings', RatingViewset)

urlpatterns = [
    path('', include(router.urls)),
]