"""pieceOfMind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from pieceOfMind_api.views import *
from pieceOfMind_api.models import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pieceUsers', PieceUserViewSet, 'pieceUser')
router.register(r'rooms', RoomViewSet, 'room')
router.register(r'collections', CollectionViewSet, 'collection')
router.register(r'items', ItemViewSet, 'item')
router.register(r'images', ImageViewSet, 'image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
