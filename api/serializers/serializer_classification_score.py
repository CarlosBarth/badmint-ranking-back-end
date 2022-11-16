from rest_framework import serializers

from api.models import Category, ClassificationScore


class ClassificationScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationScore
        fields = ('id_athlete_1', 'id_athlete_2', 'name')

