from django.shortcuts import render
from .models import *
from .forms import BookForm
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
    # Form
    if request.method == "POST":
        # variabel = request.POST["vlera e atributit name"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        comment = request.POST["comment"]
        Contact(
          contact_name =  firstname,
          contact_surname =lastname,
          contact_email=email,
          contact_comment= comment
        ).save()
    context = {"allCategory":allCategory}
    return render(request, "contact.html", context)

def menu(request):
    allCategory = Category.objects.all()
    allProduct = Product.objects.all()
    context = { "allCategory":allCategory, "allProduct":allProduct}
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
    
    
def book(request):
    allCategory = Category.objects.all()
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form = BookForm()
    context = {"allCategory":allCategory, "form":form}
    return render(request, "book.html", context)