from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ViewRankingQueryMock(GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'id': 1,
            'classification': 1,
            'scorePoints': 2780,
            'athlete1MemberID': 'ab123',
            'athlete1Name': 'Jon Snow',
            'athlete1Age': 35,
            'athlete1Club': 'IBAD',
            'athlete2MemberID': '',
            'athlete2Name': '',
            'athlete2Age': None,
            'athlete2Club': ''
        })
