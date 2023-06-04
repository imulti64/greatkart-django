from django.shortcuts import render
from store.models import Product

# 여기서 home을 함수(메서드)라 한다
def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)