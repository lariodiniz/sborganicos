#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.conf import settings
from django.test import TestCase

from model_mommy import mommy

from usuarios.models import Usuarios


class UsuariosTestCase(TestCase):
    """Clase que testa o modelo Usuario"""
    def setUp(self):
        """Método inicial"""

        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.username = 'teste'

        self.user.save()

    def tearDown(self):

        self.user.delete()

    def test_existe_usuario(self):
        """testa se esta criando usuario corretamente"""

        self.assertEquals(Usuarios.objects.count(), 1)


    def test_usuario_nome_correto(self):
        """testa se esta criando usuario corretamente"""

        user = Usuarios.objects.all()[0]
        self.assertEquals(user.username, 'teste')

    def test_usuario_verifica_senha(self):

        user = Usuarios.objects.all()[0]
        self.assertTrue(user.check_password('123'))