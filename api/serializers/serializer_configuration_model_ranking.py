from rest_framework import serializers

from api.models import Category, ConfigurationModelRanking


class ConfigurationModelRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigurationModelRanking
        fields = ('name', 'score_weeks_expiration')

