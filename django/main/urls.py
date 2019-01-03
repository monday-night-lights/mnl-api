from django.contrib import admin
from django.urls import include, path

from main.views import HomeView, APIHomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/', APIHomeView.as_view(), name='api-home'),
    # path('api/', include('teams.urls')),
]
