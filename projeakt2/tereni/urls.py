from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', views.index, name='tereni_index'),
    path('int/<int:br>',views.broj, name='tereni_broj'),
    path('int/',views.broj, name='tereni_broj_def'),
    path('params/', views.params, name='tereni_params'),
    path('hello/', views.hello, name='tereni_hello'),
]