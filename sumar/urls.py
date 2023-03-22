from django.urls import path

from . import views

urlpatterns = [
    path('<int:primernum>/<int:segundonum>', views.index, name='index'),
]