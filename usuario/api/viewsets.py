from rest_framework.viewsets import *
from rest_framework.mixins import *

from usuario.api.serializers import *

Usuario = get_user_model()


class CriarUsuarioViewSet(GenericViewSet, CreateModelMixin):
    queryset = Usuario.objects.all()
    serializer_class = CriarUsuarioSerializer
