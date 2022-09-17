from django.urls import include, path

from rest_framework.routers import SimpleRouter, Route, DynamicRoute, DefaultRouter

from bakeoff_api.views import ArtistViewSet


class BakeoffRouter(DefaultRouter):
    routes = [
        # List route.
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        DynamicRoute(
            url=r'^{prefix}/{url_path}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        # Detail route.
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
    ]


router = BakeoffRouter()

router.register(r'artists', ArtistViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
