from django import forms
from .models import Captura

class CapturaForm(forms.ModelForm):
	class Meta:
		model=Captura
		fields = ('numero_pokemon',
	    'nombre_pokemon',
	    'url_pokemon',
	    'juego',
	    'shiny',
	    'vida_pokemon',
        'ataque_pokemon',
        'defensa_pokemon',
        'ataqueesp_pokemon',
        'defensaesp_pokemon',
        'velocidad_pokemon',
        'nivel_pokemon')
		widgets = {
			'numero_pokemon':forms.HiddenInput(attrs={'id':'numero'}),
			'nombre_pokemon':forms.HiddenInput(attrs={'id':'nombre'}),
			'url_pokemon':forms.HiddenInput(attrs={'id':'url'})
		}