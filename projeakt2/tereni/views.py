from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Zdravo')


def broj(request, br=0):
    return HttpResponse('Broj: '+str(br))

def params(request):
    return HttpResponse('Params: '+str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))

def hello(request):
    return render(request, 'tereni/hello.html')