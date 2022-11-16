from rest_framework import serializers

from api.models import Athlete

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ('name', 'athlete_code', 'birth_date')

