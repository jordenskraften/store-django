from django.shortcuts import render, HttpResponse

def index(request): 
    context = {
        'title' : 'Test title',
        'is_promotion': True, 
    } 
    return render(request, 'index.html', context)

def products(request):
    context = {
        'title' : 'Store - Каталог',
        'products': [
            {
                'image': 'vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00 руб.',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': '23 725,00 руб.',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00 руб.',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
            },
            {
                'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'name': 'Черный рюкзак Nike Heritage',
                'price': '2 340,00 руб.',
                'description': 'Плотная ткань. Легкий материал.',
            }
        ]
    } 
    return render(request, 'products.html', context)

 
