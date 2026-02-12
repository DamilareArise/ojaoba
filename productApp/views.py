from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductFeatures
from .forms import ProductForm, ImageForm, FeatureForm
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from .utils import is_staff_required, is_superuser_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

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
   
# @staff_member_required(login_url="home")   
@user_passes_test(is_staff_required)
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
            
            send_mail(
                subject="New Product Alert",
                message=f"A new product has been added by {request.user.first_name} {request.user.last_name}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False
            )
            
            messages.success(request, 'Product added successfully') 
        else:
            messages.error(request, 'An error occured')
        
        return redirect('products')

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

    
    
@user_passes_test(is_staff_required)
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


@user_passes_test(is_staff_required)    
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
        
@user_passes_test(is_staff_required)       
def editProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm( request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product edited successfully')
            send_mail(
                subject="Product Edited Alert",
                message=f"Product ID0{product.id} has been edited by {request.user.first_name} {request.user.last_name}",
                from_email=f"Ojaoba <{settings.DEFAULT_FROM_EMAIL}>",
                recipient_list=[request.user.email],
                fail_silently=False
            )
        else:    
            messages.error(request, 'An error occured')
        
        return redirect("get-product", product_id)
    
    else:
        form = ProductForm(instance=product)
        return render(
            request,
            template_name="product_form.html",
            context={
                "form":form,
                "title": "Product Form"
            }
        )


@user_passes_test(is_staff_required)
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("products")