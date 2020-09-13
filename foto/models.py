from django.contrib.auth import get_user_model
from django.db import models

Usuario = get_user_model()


class Foto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='fotos')
    foto = models.ImageField(upload_to='fotos')
    data = models.DateField(auto_now_add=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.usuario, self.data)
