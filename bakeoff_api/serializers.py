from rest_framework import serializers

from bakeoff_api.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist

        fields = ('id', 'name', 'genre')
