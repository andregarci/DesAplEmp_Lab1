from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma/<int:primernum>/<int:segundonum>', views.suma, name='suma'),
    path('resta/<int:primernum>/<int:segundonum>', views.resta, name='resta'),
    path('multiplicacion/<int:primernum>/<int:segundonum>', views.multiplicacion, name='multiplicacion'),
]