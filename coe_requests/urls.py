from django.conf.urls import url

import views


urlpatterns = [
    url(
        r'create/$',
        views.request_create,
        name='request_create',
    ),
    url(
        r'platform/(?P<pk>\d+)/configuration/$',
        views.PlatformConfiguration.as_view(),
        name='platform_configuration',
    ),
    url(
        r'platform/(?P<platform_pk>\w+)/offering/(?P<offering_pk>\w+)/configuration/$',
        views.PlatformOfferingConfiguration.as_view(),
        name='platformoffering_configuration',
    ),
]
