from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from product.views import *

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CatViewSet)





urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('',include('product.url'))
    path('', include(router.urls)),
]