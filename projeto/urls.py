from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from foto.api.viewsets import FotoViewSet
from usuario.api.viewsets import CriarUsuarioViewSet, UsuarioViewSet

router = routers.DefaultRouter()
router.register('cadastro', CriarUsuarioViewSet)
router.register('fotos', FotoViewSet)
router.register('usuario', UsuarioViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls)),
                  path('login/', obtain_auth_token),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
