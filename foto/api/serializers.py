from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from foto.models import Foto


class FotoSerializer(ModelSerializer):
    foto = Base64ImageField(required=True)
    localizacao = serializers.CharField(required=False)

    class Meta:
        model = Foto
        fields = ['foto', 'localizacao', 'usuario', ]
