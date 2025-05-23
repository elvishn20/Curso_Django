from django.urls import reverse_lazy
from django.views import generic
from .forms import ProductForm
from products.models import Product


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('add_product') # Si el producto se crea hace una redireccion a esa url


    def form_valid(self, form): # Llama al metodo del formulario
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = 'products'
    
