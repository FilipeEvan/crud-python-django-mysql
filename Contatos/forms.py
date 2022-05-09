from django import forms

from .models import *

class formularioContato(forms.ModelForm):

    class Meta:
        model = Contato
        fields = (
            'nome', 
            'telefone', 
            'email', 
            'grupo',
            'endereco', 
            'numero', 
            'bairro', 
            'cep', 
            'cidade', 
            'estado'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cep'].widget.attrs.update({'class': 'mask-cep'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})

# Grupos
class formularioGrupo(forms.ModelForm):

    class Meta:
        model = Grupo
        fields = (
            'titulo',
            'descricao',
        )