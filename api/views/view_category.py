from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ViewCategoryMock(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'id': 1,
            'label': 'Ranking Estadual de Santa Catarina'
        })
