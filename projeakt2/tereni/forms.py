from django.forms import ModelForm, Form
import django.forms as f
from .models import Tereni,Ocene,Komentari


class TereniForm(ModelForm):
    class Meta:
        model = Tereni
        fields = ['naziv', 'mesto','tip','naziv_vode','korisnikVode','tip_dozvole','latituda','longituda','opis']

class OceneForm(ModelForm):
    class Meta:
        model = Ocene
        fields = ['ocena']

class KomentariForm(ModelForm):
    class Meta:
        model = Komentari
        fields = ['sadrzaj']
