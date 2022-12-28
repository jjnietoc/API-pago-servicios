
from . import api
from rest_framework import routers
from versionedPay.v2.api import PagosViewSetCustom, ServicesViewSetCustom, PaymentUserViewSetCustom, ExpiredPaymentsSerializer
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
)
from versionedPay.v2.router import api_urlpatterns as api_v2


router = routers.DefaultRouter()
router.register(r'pagos', api.PagoViewSet, 'pagos')

urlpatterns = router.urls

