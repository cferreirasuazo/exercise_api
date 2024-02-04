from rest_framework import routers
from .views import UserViewSet
from django.urls import path, include,re_path
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
]