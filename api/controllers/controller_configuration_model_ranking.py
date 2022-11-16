from api.models import ConfigurationModelRanking


def configuration_model_ranking_get_all():
    return ConfigurationModelRanking.objects.all()

