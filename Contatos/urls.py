from django.urls import path
from . import  views

urlpatterns = [
    # Contatos
    path('', views.listarContatos, name='listar-contatos'),
    path('retrieve/<int:id>', views.verContato, name='ver-contato'),
    path('create/', views.criarContato, name='criar-contato'),
    path('edit/<int:id>', views.editarContato, name='editar-contato'),
    path('delete/<int:id>', views.deletarContato, name='deletar-contato'),

    # Grupos
    path('groups/create/', views.criarGrupo, name='criar-grupo'),
]