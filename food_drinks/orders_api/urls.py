from urllib import robotparser
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerView, OrderView

router = DefaultRouter()
router.register('customer', CustomerView)
router.register('order', OrderView)

urlpatterns = [
    path('', include(router.urls)),
]
