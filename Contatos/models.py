from django.db import models

# Create your models here.
class Grupo(models.Model):
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    create_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    endereco = models.CharField(max_length=150)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    create_data = models.DateField(auto_now_add=True)
    update_data = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome