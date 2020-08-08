from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
	# add additional fields in here
	usuario_nome = models.CharField(max_length=100)
	#usuario_sobrenome = models.CharField(max_length=200)
	usuario_endereço = models.CharField(max_length=200)
	usuario_bairro = models.CharField(max_length=20)
	usuario_cidade = models.CharField(max_length=20)
	usuario_estado = models.CharField(max_length=10)
	usuario_cep = models.CharField(max_length=9)
	usuario_fone = models.CharField(max_length=20)
	
	

	def __str__(self):
		return self.id