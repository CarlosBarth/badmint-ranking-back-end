from rest_framework import serializers

from api.models import Category, Team


class TeamChampionshipStageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamChampionshipStageCategory
        fields = ('category', 'team', 'championship_sheet_importation', 'team_position_stage_category', 'team_position_category_stage', 'expiration_date', 'json_data')

