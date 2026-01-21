from django.shortcuts import render, get_object_or_404
from .models import Product, ProductFeatures

# Create your views here.


def getHome(request):
    username = "Bolaji Ogunmola"
    
    products = Product.objects.all().order_by("-created_at")
    # products = Product.objects.filter(id=1)
    # products = Product.objects.filter(title='pRoDuct 2')
    # products = Product.objects.filter(title__iexact='pRoDuct 2')
    # products = Product.objects.filter(title__exact='pRoDuct 2')
    # products = Product.objects.filter(title__icontains='pRo')
    # products = Product.objects.filter(title__contains='pRo')
    # products = Product.objects.filter(quantity__gte=10)
    # product = Product.objects.get(id=1)
    # print(product.description)
    # print(products)
    
    # product.delete()
    
    return render(
        request,
        template_name="index.html",
        context={"name": username, "products": products[0:4]}
    )


def getProducts(request):
    products = Product.objects.all().order_by("-created_at")

    return render(
        request,
        template_name="products.html",
        context={"products": products}
    )
    
def getProductbyId(request, product_id):
    # product = Product.objects.get(id=product_id)
    product = get_object_or_404(Product, id=product_id)
    return render(
        request=request,
        template_name="single_product.html",
        context={"product": product}
    )