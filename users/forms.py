from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields



class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField()
	

	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'usuario_nome',  'usuario_fone',  'usuario_endereço', 'usuario_bairro', 'usuario_cidade', 'usuario_estado', 'usuario_cep')
		labels = {'username':'Usuário', 'email': 'Email','usuario_nome':'Nome Completo', 'usuario_endereço':'Endereço', 'usuario_bairro':'Bairro', 'usuario_cidade':'Cidade', 'usuario_estado':'Estado', 'usuario_cep':'CEP', 'usuario_fone':'Fone'}
		