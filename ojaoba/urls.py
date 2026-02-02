"""
URL configuration for ojaoba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from productApp import views
from django.conf import settings
# import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.getHome, name="home"),
    path("products/", views.getProducts, name="products"),
    path("get-product/<int:product_id>/", views.getProductbyId, name="get-product"),
    path("add-product/", views.addProduct, name="add-product"),
    path("add-image/<int:product_id>/", views.addImage, name="add-image"),
    path("add-feature/<int:product_id>/", views.addFeature, name="add-feature"),
    path("edit-product/<int:product_id>/", views.editProduct, name="edit-product"),
    path("delete-product/<int:product_id>/", views.deleteProduct, name="delete-product"),
    path("accounts/", include("django.contrib.auth.urls"))
    
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

