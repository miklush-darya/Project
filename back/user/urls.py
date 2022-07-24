from django.urls import path, include
from django.conf.urls.static import static
from user.views import ShopApiView
from rest_framework import routers


router = routers.DefaultRouter()

# router.register('api/user', UserApiView.as_view({'get': 'list'}), 'user')
router.register('api/shop', ShopApiView, 'shop')

urlpatterns = router.urls


# urlpatterns = [
#     path('api/user/', UserApiView.as_view()),
#     # path('api/v3/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/products/
    
# ]