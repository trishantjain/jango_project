from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil


def index(request):
    # Fetching products from models
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def product(request, myid):
    # Fetch the product using product_id
    product = Product.objects.filter(id=myid)

    return render(request, "shop/prodView.html", {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get("itemJson", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        address = request.POST.get("address1", "") + request.POST.get("address2", "")
        state = request.POST.get("state", "")
        city = request.POST.get("city", "")
        zip_code = request.POST.get("zip_code", "")

        order = Order(item_json=item_json, name=name, email=email, phone=phone, address=address, state=state, city=city, zip_code= zip_code)
        order.save()

        thank = True
        id = order.order_id

        return render(request, "shop/checkout.html", {'thank':thank, 'id': id})
    return render(request, "shop/checkout.html")
        


