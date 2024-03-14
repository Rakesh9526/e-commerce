from django.shortcuts import render, get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

# def home(req):
#     return render(req,"base.html")

def allprodcat(req,c_slug=None):
    c_page=None
    product_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        product_list=Product.objects.all().filter(category=c_page,available=True)
    else:
        product_list=Product.objects.all().filter(available=True)
    paginator=Paginator(product_list,6)
    try:
        page=int(req.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(req,"categorypage.html",{'category':c_page,'products':products})

def productdetails(req,c_slug,p_slug):
    try:
        products=Product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(req,'product.html',{'products':products})


