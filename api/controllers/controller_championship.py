from api.models import Championship


def championship_get_all():
    return Championship.objects.all()

