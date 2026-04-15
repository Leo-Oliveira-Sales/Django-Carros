from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) # list_display define os campos que serão exibidos na lista de objetos no admin.
    search_fields = ('name',) # search_fields define os campos que serão pesquisados quando o usuário usar a barra de pesquisa no admin.

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # list_display define os campos que serão exibidos na lista de objetos no admin.
    search_fields = ('model', 'brand') # search_fields define os campos que serão pesquisados quando o usuário usar a barra de pesquisa no admin.


admin.site.register(Brand, BrandAdmin) # admin.site.register registra o modelo Brand para aparecer no admin
admin.site.register(Car, CarAdmin) # admin.site.register registra o modelo Car para aparecer no admin