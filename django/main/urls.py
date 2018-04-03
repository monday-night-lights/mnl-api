from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from .admin import mnl_admin
from .views import HomeView, APIHomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^api/?$', APIHomeView.as_view(), name='api-home'),
    url(r'^admin/', mnl_admin.urls),
    url(r'^api/auth/', include('personnel.urls')),
]
