# Create your views here.
from rest_framework import viewsets

from bakeoff_api.models import Artist
from bakeoff_api.serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
