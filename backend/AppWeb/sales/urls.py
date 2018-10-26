from . import api
from rest_framework.routers import DefaultRouter
from django.urls import include, path

app_name = 'sales'

router = DefaultRouter()
router.register(r'products', api.ProductViewSet)
router.register(r'orders', api.OrderViewSet)

apipatterns = router.urls

urlpatterns = [    
    path('api/', include(apipatterns)),
    ]