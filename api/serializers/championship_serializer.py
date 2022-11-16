from rest_framework import serializers

from api.models import Championship


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ('name', 'athlete_code', 'birth_date')

