from audioop import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_list_or_404
from django.views import View
from django.views.generic import TemplateView
from .forms import ProdutoForm
from django.template.loader import render_to_string

from .models import Produto

class DemoView(TemplateView):
    template_name = "Demo_app/index.html"

def index(request):
    return render(request,'Demo_app/index2.html')

def listar_produtos(request):
    form = ProdutoForm()
    produtos = Produto.objects.all()
    if request.method=='POST':
        criar_produto(request)
    return render(request,'Demo_app/listar_produtos.html',{'produtos':produtos,'form':form})

def save_product_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        pass
    context = {'form':form}
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

def criar_produto(request):
    data = dict()
    #O codigo do produto poderia ser gerado aleatoriamente
    #O campo "adicionado_em" vai ser automaicamente introduzido ao salvar o produto
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            produtos = Produto.objects.all()
            data['html_product_list'] = render_to_string('Demo_app/listar_produtos.html',{'produtos':produtos})
            #HttpResponseRedirect(reverse('Demo_app:listar_produto'))
        else:
            data['form_is_valid'] = False
            print("Formulario não valido, enviar mensagem de erro ou redirecionamento")
    else:
        form = ProdutoForm()
    return save_product_form(request,form,'Demo_app/criar_produto.html')

