from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tereni,Ocene,Komentari
from django.db.models import Sum
from .forms import TereniForm,OceneForm,KomentariForm

# Create your views here.
#@login_required()
def index(request):
    if request.user.is_authenticated:
        return redirect('tereni')
    else:
        return render(request, 'tereni/index.html')

def register(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('tereni')
    context['form']=form
    return render(request,'registration/register.html',context)

@login_required
def tereni(request):
    tmp = Tereni.objects.all()
    return render(request,"tereni/tereni.html",{"tereni": tmp})

@login_required
def teren(request,id):
    t = get_object_or_404(Tereni,id=id)
    #ocena filter i sum
    #testirati posle
    # o = Ocene.object.filter(teren_id = id)
    # o_sum = 0
    # o_count = o.count()
    # if (o_count>0):
    #     o_sum =

    #svi komentari
    k = Komentari.objects.filter(teren_id = id)
    return render(request,"tereni/teren.html",{"teren":t, "komentari":k,"page_title":t.naziv})

def add_teren(request):
    if request.method == 'POST':
        form = TereniForm(request.POST)

        if form.is_valid():
            t = form.save(commit=False)
            t.korisnik = request.user
            t.save()
            return redirect('tereni')
        else:
            return render(request, 'tereni/add_teren.html', {'form': form})
    else:
        form = TereniForm()
        return render(request, 'tereni/add_teren.html', {'form': form})

def add_komentar(request,t_id):

    if request.method == 'POST':
        form = KomentariForm(request.POST)

        if form.is_valid():
            t = get_object_or_404(Tereni, id=t_id)
            k = form.save(commit=False)
            k.korisnik = request.user
            k.teren = t
            k.save()
            return redirect('tereni')
        else:
            return render(request, 'tereni/add_komentar.html', {'form': form, 'id':t_id})
    else:
        #t = get_object_or_404(Tereni, id=t_id)
        form = KomentariForm()
        return render(request, 'tereni/add_komentar.html', {'form': form, 'id':t_id})

def edit_teren(request,id):
    if request.method == 'POST':
        form = TereniForm(request.POST)

        if form.is_valid():
            t = get_object_or_404(Tereni, id=id)
            t.naziv = form.cleaned_data['naziv']
            t.mesto = form.cleaned_data['mesto']
            t.tip = form.cleaned_data['tip']
            t.naziv_vode = form.cleaned_data['naziv_vode']
            t.orisnikVode = form.cleaned_data['korisnikVode']
            t.tip_dozvole = form.cleaned_data['tip_dozvole']
            t.latituda = form.cleaned_data['latituda']
            t.longituda = form.cleaned_data['longituda']
            t.opis = form.cleaned_data['opis']
            t.save()
            return redirect('tereni')
        else:
            return render(request, 'tereni/edit_teren.html', {'form': form, 'id': id})
    else:
        t = get_object_or_404(Tereni, id=id)
        form = TereniForm(instance=t)
        return render(request, 'tereni/edit_teren.html', {'form': form, 'id': id})

def edit_komentar(request,id):
    if request.method == 'POST':
        form = KomentariForm(request.POST)

        if form.is_valid():
            k = get_object_or_404(Komentari, id=id)
            k.sadrzaj = form.cleaned_data['sadrzaj']
            k.save()
            return redirect('tereni')
        else:
            return render(request, 'tereni/edit_komentar.html', {'form': form, 'id': id})
    else:
        k = get_object_or_404(Komentari, id=id)
        form = KomentariForm(instance=k)
        return render(request, 'tereni/edit_komentar.html', {'form': form, 'id': id})

#

#def delete_teren(request)




#def delete_komentar(request)

#def add_ocena(request)