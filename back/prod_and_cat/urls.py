from django.urls import path, include
from django.conf.urls.static import static
from prod_and_cat.views import CategoryApiView, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

from .views import *

urlpatterns = [
    path('api/category/', CategoryApiView.as_view()),
    path('api/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/products/
    # path('api/v3/products/', ProductApiView.as_view()),
    # path('api/v3/products/<int:pk>/', ProductApiView.as_view()),
    # path('api/v3/products/<int:pk>/', ProductApiUpdate.as_vi
    # path('api/v3/productstail/<int:pk>/', ProductApiDetailView.as_view()),

]