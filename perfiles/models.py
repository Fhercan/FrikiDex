from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

# Create your models here.
class Perfil(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
	nombre=models.CharField(max_length=250, default='')
	foto=models.ImageField(upload_to='miplace/fotos',null=True)
	pais=CountryField(null=True,blank_label="(Seleccione pais)")
	created_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.nombre+'('+self.user.username+')'

	def delete(self, using=None, keep_parents=False):
		self.foto.storage.delete(self.foto.name)
		super().delete()
		
	class Meta:
		verbose_name_plural='Perfiles'

@receiver(user_signed_up)
def createPerfil(sender=User, **kwargs):
    new_username = kwargs['user']
    user = User.objects.get(username = new_username)
    #Crear el perfil del usuario
    perfil=Perfil()
    perfil.user=user
    perfil.nombre=user.username
    perfil.pais=None
    perfil.save()
    print(perfil)