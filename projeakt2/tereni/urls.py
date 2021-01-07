from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.index, name='tereni_index'),
    path('register/',views.register,name="register"),
    #prikaz svih terena
    #prikaz pojedinacnih terena sa komentarima i ocenama
    #dodavanje terena, komentara, ocene
    #izmena terena, komentara i ocena
    #path('int/<int:br>',views.broj, name='tereni_broj'),
    # path('int/',views.broj, name='tereni_broj_def'),
    # path('params/', views.params, name='tereni_params'),
    # path('hello/', views.hello, name='tereni_hello'),
]