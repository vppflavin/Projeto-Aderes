from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel nome de referência
    path('',views.home,name='home'),
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    path('deletarUser/<int:id>', views.deletarUser, name='deletarUser'),
    path('updateEdit/<int:id>/', views.updateEdit, name='updateEdit'),
]

