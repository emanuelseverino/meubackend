from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import *


from foto.api.serializers import *

Usuario = get_user_model()


class FotoViewSet(ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        usuario = self.request.user
        return self.queryset.filter(usuario=usuario)
