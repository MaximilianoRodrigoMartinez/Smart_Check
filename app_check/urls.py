from django.urls import path
from app_check.views import inicio, crea_local, lista_locales, crea_empleado, lista_empleados, asigna_horarios, lista_horarios, login_view, logout_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('inicio', inicio, name="Inicio"),
    path('crea-local/', crea_local,name="Crea_local"),
    path('lista-locales/', lista_locales, name="Lista_locales"),
    path('crea-empleado/', crea_empleado, name="Crea_empleado"),
    path('lista-empleados/', lista_empleados, name="Lista_empleados"),
    path('asigna-horarios/', asigna_horarios, name="Asigna_horarios"),
    path('lista-horarios/', lista_horarios, name="Lista_horarios"),
    path('ingresar/', login_view, name='Login_view'),
    path('salir/', logout_view, name='Logout_view'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)