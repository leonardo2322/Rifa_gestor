from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView,View
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from time import sleep
from decimal import Decimal
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q
from .models import Cliente
from .forms import Form_creacion_jugador,Form_abonos
def home(request):
    return render(request,"Base.html")
# Create your views here.
class Creacion_de_jugador(CreateView):
    model = Cliente
    form_class = Form_creacion_jugador
    template_name = "creacion_cliente.html"
    success_url = reverse_lazy('crear')

    def form_valid(self, form):
        estado = form.save()
        messages.success(self.request, 'El jugador ha sido creado correctamente')
        return super().form_valid(form)
    def form_invalid(self, form):
        
        non_field_errors = form.errors.get('__all__', [])
        if non_field_errors:
            for error in non_field_errors:
                messages.error(self.request, f"Error: {error}")
        else:
            messages.error(self.request, f'Error al crear el jugador, {form.errors}')
        return super().form_invalid(form)


class Listado_de_juadores_view(ListView):
    model = Cliente
    template_name = "Listado.html"
    context_object_name = "jugadores"
    paginate_by = 10
    
    def get_queryset(self):
        search = self.request.GET.get('q', '')  # Captura el valor del input de búsqueda
        estado = self.kwargs.get('estado')  # Captura el estado de la URL

        # Iniciar queryset con todos los clientes
        queryset = Cliente.objects.all()

        # Filtrar por estado si se proporciona en la URL
        if estado == 'Cancelados':
            queryset = queryset.filter(estado=True)
        elif estado == 'Por Pagar':
            queryset = queryset.filter(estado=False)
        elif estado == 'Abonos':
            queryset = queryset.filter(abono__gt=0, estado=False)

        # Si hay búsqueda, filtrar por nombre, pero sin eliminar otros filtros previos
        if search:
            queryset = queryset.filter(Q(nombre__icontains=search) | Q(telefono__icontains=search))

        # Ordenar por fecha_registro
        queryset = queryset.order_by('fecha_registro')


        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_dinero = Cliente.objects.filter(abono__gt=0,estado=False).aggregate(total_abono=Sum('abono'))['total_abono']
        tikets_cancelados = Cliente.objects.filter(estado=True).values('numeros')
        clientes = Cliente.objects.all()
        numeros_vendidos =  sum(len(cliente.numeros) for cliente in clientes if cliente.numeros)
       
        for ticket in tikets_cancelados:
            numeros = ticket['numeros']
            if isinstance(numeros, str):
                import json

                numeros = json.loads(ticket['numeros']) 
            cantidad_numeros = len(numeros)
            if cantidad_numeros == 3:
                total_dinero += 5
            elif cantidad_numeros > 3 and cantidad_numeros < 6:
                total_dinero += 5 + ((cantidad_numeros - 3) * 2)
            elif cantidad_numeros == 6:
                total_dinero += 10
            else:
                total_dinero += cantidad_numeros * 2

        context['total_dinero'] = total_dinero 
        context['numeros_totales'] = numeros_vendidos
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['jugadores'] = page_obj
        return context


def template_abono(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render (request,'abono.html',{'cliente':cliente})


def guardar_abono(request, pk):
    # Obtener el cliente por su ID
    cliente = get_object_or_404(Cliente, pk=pk)
    nuevo_abono = request.POST.get('abono')
    try:
        # Convertir el valor a decimal
        nuevo_abono = Decimal(nuevo_abono)
        
        # Actualizar el campo "abono" sumando el nuevo valor
        cliente.abono += nuevo_abono
        cliente.save()
        
        # Mostrar mensaje de éxito
        messages.success(request, 'El abono ha sido actualizado correctamente.')
    except (ValueError, TypeError) as e:
        # Mostrar mensaje de error si el valor no es válido
        messages.error(request, f'El valor del abono no es válido.{e}')
    
    # Redirigir a la página de listado (o a donde necesites)
    estado = 'Todos'  # O el valor que desees pasar
    return redirect('listado', estado=estado)

class Actualizar_jugador_view(UpdateView):
    model = Cliente
    form_class = Form_creacion_jugador
    template_name = "actualizacion.html"
    
    def get_success_url(self):
        estado = self.kwargs.get('estado', 'Todos')
        return reverse_lazy('listado', kwargs={'estado': estado})
    def form_valid(self, form):
        messages.success(self.request, 'El jugador ha sido actualizado correctamente')
        return super().form_valid(form)
    

class Eliminar_jugador_view(View):
    def post(self,request, *args, **kwargs):
        try:
            cliente = get_object_or_404(Cliente, pk=kwargs['pk'])
            cliente.delete()
            messages.success(request, 'El jugador  ha sido eliminado correctamente')
            estado = kwargs.get('estado', 'Todos')
            return redirect(reverse('listado', kwargs={'estado': estado}))
        except Exception as e:
            messages.error(request, f'Error al eliminar el jugador: {str(e)}')
            estado = kwargs.get('estado', 'Todos')
            return redirect(reverse('listado', kwargs={'estado': estado}))