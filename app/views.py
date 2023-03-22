from django.http import HttpResponse

def index(request):
    return HttpResponse(" sumar/x/y , restar/x/y, multiplicar/x/y")
def suma(request, primernum, segundonum):
    suma = primernum + segundonum
    return HttpResponse("La suma de {} y {} es  {}".format(primernum,segundonum,suma))
def resta(request, primernum, segundonum):
    resta = primernum - segundonum
    return HttpResponse("La resta de {} y {} es  {}".format(primernum,segundonum,resta))
def multiplicacion(request, primernum, segundonum):
    multiplicacion = primernum * segundonum
    return HttpResponse("La multiplicacion de {} y {} es  {}".format(primernum,segundonum,multiplicacion))