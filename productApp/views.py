from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductFeatures
from .forms import ProductForm, ImageForm, FeatureForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def getHome(request):
    username = "Bolaji Ogunmola"
    
    products = ( Product.objects
                .all() 
                .prefetch_related(
                    "features",
                    "images",
                    "reviews"
                )
                .order_by("-created_at")
            )

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
    products = ( Product.objects
                .all() 
                .prefetch_related(
                    "features",
                    "images",
                    "reviews"
                )
                .order_by("-created_at")
            )
    # print(products)
    # for prod in products:
    #     print(prod.images.all().first().image.url)
    
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
   
@login_required    
def addProduct(request):
    # print(request.user.email)
    
    if request.method == "POST":
        # print(request.POST.get("title"))
        # Product.objects.create(
        #     title = request.POST.get("title")
        # )
        
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
        
        return redirect("products")

    else:
        form = ProductForm()
        return render(
            request,
            template_name="product_form.html",
            context={
                "form":form,
                "title": "Product Form"
            }
        )
    
def addImage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
            
        return redirect("get-product", product_id)
    else:
        form = ImageForm()
        return render(
            request,
            template_name="product_form.html",
            context={
                "form":form,
                "title": "Upload Image"
            }
        )
    
def addFeature(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = FeatureForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
            
        return redirect("get-product", product_id)
    else:
        form = FeatureForm()
        return render(
            request,
            template_name="product_form.html",
            context={
                "form":form,
                "title": "Feature Form"
            }
        )