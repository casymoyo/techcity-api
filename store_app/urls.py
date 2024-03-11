from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  

router = DefaultRouter()
router.register('users', views.UserListView, basename='users')
router.register('stores', views.StoreViewSet, basename='stores')

urlpatterns = [
    path('', include(router.urls)),
]
