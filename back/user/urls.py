from django.urls import path, include
from django.conf.urls.static import static
from user.views import UserApiView
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'products', ProductViewSet)


urlpatterns = [
    path('api/user/', UserApiView.as_view()),
    # path('api/v3/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/products/
    

]