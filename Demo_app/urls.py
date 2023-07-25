from . import views
from django.urls import path

app_name = 'Demo_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('listar-produtos',views.listar_produtos,name='listar_produtos'),
    path('criar-produto',views.criar_produto,name='criar_produto'),
]