from api.models import Ranking


def ranking_get_all():
    return Ranking.objects.all()

