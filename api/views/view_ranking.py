from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ViewRankingMock(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'id': 1,
            'label': 'Masculino Duplas Sub-17'
        })
