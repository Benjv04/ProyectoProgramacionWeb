from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name = 'index'),
    path('carrito', views.carrito, name = 'carrito'),
    path('contacto', views.contacto, name = 'contacto'),
    path('gatos', views.gatos, name = 'gatos'),
    path('inicioSesion', views.inicioSesion, name = 'inicioSesion'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('otros', views.otros, name = 'otros'),
    path('perros', views.perros, name = 'perros'),
    path('register', views.register, name = 'register'),
    path('seguimiento', views.seguimiento, name = 'seguimiento'),
    path('usuario_form', views.usuario_form, name = 'usuario_form'),
]