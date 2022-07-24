from django.urls import path, include
from django.conf.urls.static import static
from .views import OrderApiView, ShopProductOrderSerializer
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/order', OrderApiView, 'order')
router.register('api/orderproducts', ShopProductOrderSerializer, 'products')

urlpatterns = router.urls