from django.shortcuts import render, get_object_or_404
from django.template import loader
#from django.http import Http404
# Create your views here.

from django.http import HttpResponse
from .models import Product

def index(request):
    #return HttpResponse("Hello, world. You're at the reviews index.")
    '''productList = Product.objects.order_by('-name')[:5]
    template = loader.get_template('index.html')
    context = {
        'productList': productList,
    }
    return HttpResponse(template.render(context, request))'''
    productList = Product.objects.order_by('-name')[:5]
    context = {'productList': productList}
    return render(request, 'index.html', context)
    #output = ', '.join([q.name for q in productList])
    #return HttpResponse(output)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product})
    #try:
       # product = Product.objects.get(pk=product_id)
        #except Product.DoesNotExist:
          #  raise Http404("Product does not exist")
        #return render(request, 'product.html', {'Product': product})
    #return HttpResponse("You're looking at product %s." % product_id)

def reviews(request, review_id):
    response = "You're looking at the results of review %s."
    return HttpResponse(response % review_id)

def add_review(request, review_id):
    return HttpResponse("You're adding a review to product %s." % review_id)