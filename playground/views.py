from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
# Create your views here.
from store.models import Product,OrderItem





def say_hello(request):
    # query_set = Product.objects.all()
    # for product in query_set:
    #     print(product)
    # try:
    #     product = Product.objects.get(pk = 0)
    # except ObjectDoesNotExist :
    #     pass
    
    # exists = Product.objects.filter(pk=0).exists()
    # query_set = Product.objects.filter(Q(inventory__lt = 0)|Q(inventory__gt = 100))
    # query_set = Product.objects.filter(inventory = F('collection_id'))
    query_set = Product.objects.filter(id__in = OrderItem.objects.values('product_id').distinct()).order_by('title')



    return render(request, "hello.html",{'name':'Abhishek Raj','products':list(query_set)})