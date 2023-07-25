from django import forms
from .models import Produto

#create yout forms here

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ("nome","codigo_produto", "preco","quantidade","categoria_tipo")

    
