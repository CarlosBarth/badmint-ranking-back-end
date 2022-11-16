from rest_framework import serializers

from api.models import ChampionshipSheetImportation


class ChampionshipSheetImportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionshipSheetImportation
        fields = ('importation_date_time', 'file_name', 'file')

