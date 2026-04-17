from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView


# Views como classe:

# class CarsView(View):

#     def get(self, request):
#         cars = Car.objects.all().order_by("model")  # Ordena os carros por data de criação
#         search = request.GET.get("search")  # Obtém o valor do parâmetro de busca da URL
#         if search:
#             cars = cars.filter(model__icontains=search)  # Filtra os carros pelo modelo, usando uma busca case-insensitive
#         return render(request, "cars.html", {"cars": cars}) # Renderiza o template "cars.html" e passa a lista de carros filtrada como contexto para o template


class CarsListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")  # Ordena os carros por modelo
        search = self.request.GET.get("search") # Busca

        if search:
            cars = cars.filter(model__icontains=search)  # Filtra os carros pelo modelo, usando uma busca case-insensitive
        return cars  # Retorna a queryset de carros filtrada para ser usada no template


# class NewCarView(View):

#     def get(self, request):
#         new_car_form = CarModelForm()  
#         return render(request, "new_car.html", {"new_car_form": new_car_form})
    
#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES) # Recebe os Dados e Arquivos do formulário
#         if new_car_form.is_valid():  # Verifica se o formulário é válido
#             new_car_form.save()  # Salva o novo carro no banco de dados se for válido
#             return redirect("cars_list")  # Redireciona para a lista de carros após salvar o novo carro
#         return render(request, "new_car.html", {"new_car_form": new_car_form})


class newCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"  # Redireciona para a lista de carros após criar um novo carro



