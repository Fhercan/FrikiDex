from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from logros.models import Logro

# Create your models here.
class Megusta(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	logro=models.ForeignKey(Logro, on_delete=models.CASCADE)
	estatus_megusta=models.BooleanField(default=True)
	created_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.username+'-'+self.logro.titulo

	class Meta:
		verbose_name_plural='Megusta'