from django.db import models

# Criando a Tabela.


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name # Vai retornar o nome da marca, e não mais Brand object (1), Brand object (2) etc.

# blank=True permite que o campo seja deixado em branco, null=True permite que o campo seja nulo.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # ForeignKey é um campo de chave estrangeira, on_delete=models.PROTECT impede que a marca seja deletada se houver um carro associado a ela, related_name é o nome do relacionamento.
    factory_year = models.IntegerField(blank=True, null=True) 
    model_year = models.IntegerField(blank=True, null=True) 
    plate = models.CharField(max_length=10, blank=True, null=True) 
    value = models.FloatField(blank=True, null=True) 
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # ImageField é um campo de imagem, upload_to é o diretório onde as imagens serão armazenadas

    def __str__(self):
        return self.model # Vai retornar o nome do modelo do carro, e não mais Car object (1), Car object (2) etc.