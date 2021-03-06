from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
from .models import Product


def product_list(request):

    product_list = Product.objects.all()

    paginator = Paginator(product_list, 2)  # Show 2 contacts per page
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list': product_list}
    return render(request, 'product/product_list.html', context)


def product_detail(request, id):
    # prodcut_detail = Product.objects.get(PRDSLug=slug)
    prodcut_detail = get_object_or_404(Product, id=id)
    context = {'prodcut_detail': prodcut_detail}
    return render(request, 'Product/product_detail.html', context)
