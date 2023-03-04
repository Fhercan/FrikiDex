from django.test import TestCase
from django.contrib.auth.models import User
from .models import Perfil

# Create your tests here.
class TestPerfil(TestCase):

    def setUp(self)-> None:
        pass
    
    #Verificar que al crear un usuario se cree un perfil
    def test_crear_perfil(self):
        self.client.post('/accounts/signup/',{'username':'Usuarioprueba','email':'usuario@prueba.com','password1':'Up123456','password2':'Up123456'})
        newUser=User.objects.filter(username='Usuarioprueba').first()
        perfil=Perfil.objects.filter(user=newUser).first()
        self.assertIsInstance(perfil,Perfil)

    def tearDown(self):
        pass