from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Brand', views.BrandViewSet)
router.register(r'Item', views.ItemViewSet)
router.register(r'Order', views.OrderViewSet)
router.register(r'OrderItem', views.OrderItemViewSet)
router.register(r'Transfer', views.TransferViewSet)
router.register(r'TransferItems', views.TransferItemViewSet)
router.register(r'Customer', views.CustomerViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]