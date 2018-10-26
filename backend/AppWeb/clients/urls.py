from . import api
from rest_framework.routers import DefaultRouter
from django.urls import include, path

app_name = 'clients'

router = DefaultRouter()
router.register(r'clients', api.ClientViewSet)

apipatterns = router.urls

urlpatterns = [    
    path('api/', include(apipatterns)),
    ]