from django.urls import path
from .views import home, Creacion_de_jugador, Listado_de_juadores_view, Actualizar_jugador_view, Eliminar_jugador_view,guardar_abono,template_abono
urlpatterns = [
    path('', home,name='inicio'),

    path('creacion/', Creacion_de_jugador.as_view(), name='crear'),
    path('listado/<str:estado>/',Listado_de_juadores_view.as_view(),name='listado'),
    path("abonar/<int:pk>/", template_abono, name="abonar"),
    path("guardar/<int:pk>/", guardar_abono, name="guardar"),

    path("actualizar/<int:pk>/", Actualizar_jugador_view.as_view(), name='actualizar'),
    path("eliminar/cliente/<int:pk>/", Eliminar_jugador_view.as_view(), name="Eliminar")
]