from django.contrib import admin
from django.urls import path, include
from server.views import UserViewSet, index, DadoViewSet, SinalViewSet
from server import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'dados', DadoViewSet)
router.register(r'sinal', SinalViewSet)
#router.register(r'user', UserList)
#router.register(r'user', UserList)



urlpatterns = [
    path('api/', include(router.urls)),
    path('', index),
    path('admin/', admin.site.urls),
    #path('api/', include('rest_framework.urls')),
    path('username/', UserViewSet.as_view(), name='username'),
]
