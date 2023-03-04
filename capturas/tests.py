from django.test import RequestFactory, TestCase

from .views import editarCaptura
from .models import Captura
from logros.models import Logro
from django.contrib.auth.models import User

# Create your tests here.
class TestPerfil(TestCase):

    def setUp(self)-> None:
        self.request_factory = RequestFactory()
        self.testUser=User.objects.create_user(email='usuario@prueba.com',username='prueba',password='123',is_superuser=True,is_staff=True)
        self.testUser.save()
    
    def test_user_create(self):
        self.assertEqual(self.testUser.id,1)

    #Verificar que al crear una captura se cree un logro
    def test_crear_logro_captura(self):
        #self.client.login(username='prueba',password='123')
        
        pass
        #request = self.request_factory.post('/capturas/editar/0', {'numero_pokemon':1,
	    #'nombre_pokemon':'bulbasaur',
	    #'url_pokemon':'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png',
	    #'juego':1,
	    #'shiny':'on',
	    #'vida_pokemon':0,
        #'ataque_pokemon':0,
        #'defensa_pokemon':0,
        #'ataqueesp_pokemon':0,
        #'defensaesp_pokemon':0,
        #'velocidad_pokemon':0,
        #'nivel_pokemon':0
        #})
        #request.user = self.testUser
        #response=editarCaptura(request, 0)
        #newCaptura=Captura.objects.filter(numero_pokemon=1).first()
        #self.assertIsInstance(newCaptura,Captura)
        #logro=Logro.objects.filter(captura=newCaptura).first()
        #self.assertIsInstance(logro,Logro)

    def tearDown(self):
        pass