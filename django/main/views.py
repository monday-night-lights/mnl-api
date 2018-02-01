from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class APIHome(APIView):
    '''
    This is the beginning of the MNL API. There's nothing here yet.
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response()
