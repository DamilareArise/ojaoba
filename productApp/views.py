from django.shortcuts import render

# Create your views here.

products = [
        {
            "name": "Product 1",
            "price": 100,
            "description": "Product 1 description",
            "image": "https://tse4.mm.bing.net/th/id/OIF.jMp6cNMJwCbKDHwMN3Uqmw?rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        {
            "name": "Product 2",
            "price": 200,
            "description": "Product 2 description",
            "image": "https://d2v5dzhdg4zhx3.cloudfront.net/web-assets/images/storypages/primary/ProductShowcasesampleimages/JPEG/Product+Showcase-1.jpg"
        },
        {
            "name": "Product 3",
            "price": 300,
            "description": "Product 3 description",
            "image": "https://tse2.mm.bing.net/th/id/OIP.WWJfnkziSFoYhdJ-3wDV9QHaLH?rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        {
            "name": "Product 4",
            "price": 400,
            "description": "Product 4 description",
            "image": "https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?cs=srgb&dl=pexels-madebymath-90946.jpg&fm=jpg"
        },
        {
            "name": "Product 1",
            "price": 100,
            "description": "Product 1 description",
            "image": "https://tse4.mm.bing.net/th/id/OIF.jMp6cNMJwCbKDHwMN3Uqmw?rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        {
            "name": "Product 2",
            "price": 200,
            "description": "Product 2 description",
            "image": "https://d2v5dzhdg4zhx3.cloudfront.net/web-assets/images/storypages/primary/ProductShowcasesampleimages/JPEG/Product+Showcase-1.jpg"
        },
        {
            "name": "Product 3",
            "price": 300,
            "description": "Product 3 description",
            "image": "https://tse2.mm.bing.net/th/id/OIP.WWJfnkziSFoYhdJ-3wDV9QHaLH?rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        {
            "name": "Product 4",
            "price": 400,
            "description": "Product 4 description",
            "image": "https://images.pexels.com/photos/90946/pexels-photo-90946.jpeg?cs=srgb&dl=pexels-madebymath-90946.jpg&fm=jpg"
        }
    ]

def getHome(request):
    username = "Bolaji Ogunmola"
    
    return render(
        request,
        template_name="index.html",
        context={"name": username, "products": products[0:4]}
    )


def getProducts(request):
    
    return render(
        request,
        template_name="products.html",
        context={"products": products}
    )