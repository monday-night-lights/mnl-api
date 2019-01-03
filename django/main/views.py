from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

# from teams.models import Team


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        # teams = Team.objects.all().order_by('?')
        return render(request, self.template_name, {'teams': ['teams']})


class APIHomeView(APIView):
    '''
    [Back to Site Homepage](/)

    '''
    # # API Endpoints
    # - [Teams](/api/teams/)

    def get(self, request, format=None):
        return Response()
