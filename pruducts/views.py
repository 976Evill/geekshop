from django.shortcuts import render


from pruducts.models import Product,ProductCategory
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': [
            {
                "name": "Худи черного цвета с монограммами adidas Originals",
                "image": "products_images/Adidas-hoodie.png",
                "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
                "price": "6090.00"
            },
            {
                "name": "Синяя куртка The North Face",
                "image": "products_images/Blue-jacket-The-North-Face.png",
                "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пухов",
                "price": "23725.00"
            },
            {
                "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
                "image": "products_images/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
                "price": "3390.00"
            },
            {
                "name": "Синяя куртка The North Face",
                "image": "products_images/Blue-jacket-The-North-Face.png",
                "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пухов",
                "price": "23725.00"
            },
            {
                "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
                "image": "products_images/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
                "price": "3390.00"
            },
            {
                "name": "Черный рюкзак Nike Heritage",
                "image": "products_images/Black-Nike-Heritage-backpack.png",
                "description": "Плотная ткань. Легкий материал.",
                "price": "2340.00"
            },
            {
                "name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
                "image": "products_images/Black-Dr-Martens-shoes.png",
                "description": "Гладкий кожаный верх. Натуральный материал.",
                "price": "13590.00"
            },
            {
                "name": "Темно-синие широкие строгие брюки ASOS DESIGN",
                "image": "products_images/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
                "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
                "price": "2890.00"
            }

        ]
    }
    return render(request, 'products/products.html', context)

