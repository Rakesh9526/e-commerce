from django.shortcuts import render
from e_app.models import Product,Category
from django.db.models import Q

# Create your views here.

def searchresult(req):
    products=None
    query=None
    if 'q' in req.GET:
        query=req.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(req,"search.html",{'query':query,'products':products})
