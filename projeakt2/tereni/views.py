from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required()
def index(request):
    if request.user.is_authenticated:
        return render(request, 'tereni/hello.html')
    else:
        return render(request, 'tereni/hello.html')

def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'tereni/index.html')
    context['form']=form
    return render(request,'registration/register.html',context)


# def broj(request, br=0):
#     return HttpResponse('Broj: '+str(br))
#
# def params(request):
#     return HttpResponse('Params: '+str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))
#
# def hello(request):
#     return render(request, 'tereni/hello.html')