from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

SwaggerSchemaView = get_schema_view(
    openapi.Info(
        title="Badmint",
        default_version='v1',
        description="Documentação da API responsável pela gestão de ranking de Badminton",
        contact=openapi.Contact(email='thiagoarturschumann@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
