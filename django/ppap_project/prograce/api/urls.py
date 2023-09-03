from django.urls import path, include
from rest_framework import routers
from prograce.api.views import OrderListDataViewSet, SupplierDataViewSet, WorkNameDataViewSet

router = routers.DefaultRouter()
router.register('orderlistdata', OrderListDataViewSet)
router.register('supplierdata', SupplierDataViewSet)
router.register('worknamedata', WorkNameDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

