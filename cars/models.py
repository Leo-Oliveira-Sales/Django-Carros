from django.db import models

# Criando a Tabela.
class Car(models.Model):
    id = models.AutoField(primary_key=True) # AutoField é um campo de auto incremento /número único para cada registro.
    model = models.CharField(max_length=200) # CharField é um campo de texto, max_length é o tamanho máximo do texto.
    brand = models.CharField(max_length=200) # CharField é um campo de texto, max_length é o tamanho máximo do texto.
    factory_year = models.IntegerField(blank=True, null=True) # IntegerField é um campo de número inteiro.
    year = models.IntegerField(blank=True, null=True) # IntegerField é um campo de número inteiro.
    value = models.FloatField(blank=True, null=True) # FloatField é um campo de número decimal, blank=True permite que o campo seja deixado em branco, null=True permite que o campo seja nulo.

