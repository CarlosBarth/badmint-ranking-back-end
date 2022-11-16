from api.models import Athlete

def category_get_all():
    return Athlete.objects.all()

