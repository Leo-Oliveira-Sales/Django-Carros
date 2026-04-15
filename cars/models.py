from django.db import models

# Criando a Tabela.


class Brand(models.Model):
    id = models.AutoField(primary_key=True) # AutoField é um campo de auto incremento /número único para cada registro.
    name = models.CharField(max_length=200) # CharField é um campo de texto, max_length é o tamanho máximo do texto.

    def __str__(self):
        return self.name # Vai retornar o nome da marca, e não mais Brand object (1), Brand object (2) etc.


class Car(models.Model):
    id = models.AutoField(primary_key=True) # AutoField é um campo de auto incremento /número único para cada registro.
    model = models.CharField(max_length=200) # CharField é um campo de texto, max_length é o tamanho máximo do texto.
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # ForeignKey é um campo de chave estrangeira, on_delete=models.PROTECT impede que a marca seja deletada se houver um carro associado a ela, related_name é o nome do relacionamento.
    factory_year = models.IntegerField(blank=True, null=True) # IntegerField é um campo de número inteiro.
    model_year = models.IntegerField(blank=True, null=True) # IntegerField é um campo de número inteiro.
    value = models.FloatField(blank=True, null=True) # FloatField é um campo de número decimal, blank=True permite que o campo seja deixado em branco, null=True permite que o campo seja nulo.

    def __str__(self):
        return self.model # Vai retornar o nome do modelo do carro, e não mais Car object (1), Car object (2) etc.