from api.models import Category

def category_get_all():
    return Category.objects.all()

