from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from capturas.models import Captura

# Create your models here.
class Logro(models.Model):
	titulo=models.CharField(verbose_name='Título',max_length=250)
	foto=models.ImageField(upload_to='fotos',null=True)
	comentarios=models.TextField(null=True)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	megustas=models.IntegerField(default=0)
	nomegusta=models.IntegerField(default=0)
	captura=models.ForeignKey(Captura, null=True, on_delete=models.CASCADE)
	publicar=models.BooleanField(default=False)
	created_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo

	def delete(self, using=None, keep_parents=False):
		self.foto.storage.delete(self.foto.name)
		super().delete()

	class Meta:
		verbose_name_plural='Logros'