from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    # emerVaribli = EmriClass.objects.metoden
    # marrja e te gjithave informacioneve nga class => .all()
    # .all() => ciklin for in tek html per te afishuar informacionet
    allServices = Service.objects.all()
    allCategory = Category.objects.all()
    context = {"allServices":allServices, "allCategory":allCategory}
    return render(request, "home.html", context)

def about(request):
    allServices = Service.objects.all()
    allCategory = Category.objects.all()
    context = {"allServices":allServices, "allCategory":allCategory}
    return render(request, "about.html", context)

def contact(request):
    allCategory = Category.objects.all()
    context = {"allCategory":allCategory}
    return render(request, "contact.html", context)

def menu(request):
    allCategory = Category.objects.all()
    context = { "allCategory":allCategory}
    return render(request, "menu.html", context)

def category(request, slug):
    allCategory = Category.objects.all()
    # .get merr vetem nje informacion
    getCategory = Category.objects.get(category_slug=slug)
    # .filter, merr te gjitha e elementet qe plotesojne kushtin => for in tek html
    productsCategory = Product.objects.filter(product_category=getCategory)
    context = {"getCategory":getCategory, "allCategory":allCategory, "productsCategory":productsCategory}
    return render(request, "category.html", context)

def product(request, slug):
    allCategory = Category.objects.all()
    getProduct = Product.objects.get(product_slug=slug)
    context = {"allCategory":allCategory, "getProduct":getProduct}
    return render(request, "product.html", context)
    