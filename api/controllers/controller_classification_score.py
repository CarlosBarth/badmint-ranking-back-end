from api.models import ClassificationScore


def classification_score_get_all():
    return ClassificationScore.objects.all()

