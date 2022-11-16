from api.models import Team


def team_get_all():
    return Team.objects.all()

