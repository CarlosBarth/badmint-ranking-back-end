from api.models import TeamChampionshipStageCategory


def team_championship_stage_category_get_all():
    return TeamChampionshipStageCategory.objects.all()

