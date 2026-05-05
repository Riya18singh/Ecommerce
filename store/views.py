from django.http import JsonResponse
from .models import Product, Chat

def chatbot(request):
    query = request.GET.get('q')

    products = Product.objects.filter(name__icontains=query)

    if products.exists():
        result = []
        for p in products:
            result.append({
                'name': p.name,
                'price': p.price,
                'description': p.description
            })
        return JsonResponse({'response': result})
    else:
        return JsonResponse({'response': "No product found"})