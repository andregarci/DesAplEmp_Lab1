from django.http import HttpResponse

def index(request, primernum, segundonum):
    suma = primernum + segundonum
    return HttpResponse("La suma de {} y {} es  {}".format(primernum,segundonum,suma))