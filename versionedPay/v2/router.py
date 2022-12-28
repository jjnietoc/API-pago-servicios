from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pagos', api.PagosViewSetCustom, 'pagosCustom')
router.register(r'servicios', api.ServicesViewSetCustom, 'serviciosCustom')
router.register(r'usuario-pagos', api.PaymentUserViewSetCustom, 'usuariopCustom')
router.register(r'pagos-expirados', api.ExpiredViewSetCustom, 'pagosexpCustom')

api_urlpatterns = router.urls