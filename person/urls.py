from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.conf import settings
from .views import MyUserViewSet, TempAPIView


router = DefaultRouter(trailing_slash=True)
router.register(r'myuser', MyUserViewSet, 'api-products')


def get_api_url(name='api', version=settings.API_VERSION, app_name='', url_name=''):
    url = '{0}/{1}/'.format(name, version)

    if app_name and url_name:
        url = '{0}{1}/{2}/'.format(url, app_name, url_name)

    elif app_name and not url_name:
        url = '{0}{1}/'.format(url, app_name)

    elif url_name and not app_name:
        url = '{0}{1}/'.format(url, url_name)

    return url


urlpatterns = [
    path(get_api_url(), include(router.urls)),
    path('temp/', TempAPIView.as_view())
]