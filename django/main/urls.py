from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from .admin import mnl_admin
from .views import APIHome

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='admin:index'), name='home'),
    url(r'^api/?$', APIHome.as_view(), name='api-home'),
    url(r'^admin/', mnl_admin.urls),
    url(r'^api/auth/', include('users.urls')),
]
