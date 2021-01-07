from django.contrib import admin
from .models import Tereni,Ocene,Komentari
# Register your models here.


admin.site.register(Tereni)
admin.site.register(Komentari)
admin.site.register(Ocene)