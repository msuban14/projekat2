from django.template.defaulttags import url
from django.urls import path
from . import views

#app_name = "tereni"
urlpatterns = [

    path('', views.index, name='tereni_index'),
    path('register/',views.register,name="register"),
    path('tereni/', views.tereni, name='tereni'),
    path('tereni/<int:id>/', views.teren, name='teren'),
    path('tereni/add/', views.add_teren, name='add_teren'),
    path('tereni/add_komentar/<int:t_id>', views.add_komentar, name='add_komentar'),
    path('tereni/edit/<int:id>', views.edit_teren, name='edit_teren'),
    path('tereni/edit_komentar/<int:id>', views.edit_komentar, name='edit_komentar'),
    path('tereni/delete/<int:id>', views.delete_teren1, name='delete_teren'),
    path('tereni/delete_komentar/<int:id>', views.delete_komentar, name='delete_komentar')





    #dodavanje terena, komentara, ocene
    #izmena terena, komentara i ocenatar

]