from api.models import ChampionshipSheetImportation


def championship_sheet_importation_get_all():
    return ChampionshipSheetImportation.objects.all()

