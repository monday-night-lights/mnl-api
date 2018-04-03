from django.views.generic.base import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_articles'] = Article.objects.all()[:5]
        return context


class APIHomeView(APIView):
    '''
    This is the beginning of the MNL API. There's nothing here yet.
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response()
