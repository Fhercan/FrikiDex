from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Juego(models.Model):
	titulo=models.CharField(max_length=250,default='')
	urlportada=models.CharField(max_length=250,default='')
	lanzamiento=models.CharField(max_length=25,default='')
	plataforma=models.CharField(max_length=50,default='')
	created_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name_plural='Juegos'

class Captura(models.Model):
	numero_pokemon=models.IntegerField(verbose_name='Número',default=0)
	nombre_pokemon=models.CharField(verbose_name='Nombre',max_length=250)
	vida_pokemon=models.IntegerField(verbose_name='Vida',default=0)
	ataque_pokemon=models.IntegerField(default=0)
	defensa_pokemon=models.IntegerField(default=0)
	ataqueesp_pokemon=models.IntegerField(default=0)
	defensaesp_pokemon=models.IntegerField(default=0)
	velocidad_pokemon=models.IntegerField(default=0)
	nivel_pokemon=models.IntegerField(default=0)
	url_pokemon=models.CharField(max_length=250, default='')
	comentarios=models.TextField(null=True)
	shiny=models.BooleanField(default=False)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	juego=models.ForeignKey(Juego, on_delete=models.CASCADE)
	created_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return 'No.'+str(self.numero_pokemon)+' '+self.nombre_pokemon

	class Meta:
		verbose_name_plural='Capturas'
