from django.shortcuts import render,get_object_or_404
from sellers.models import Seller


# Create your views here.
def sellers(request):
    sellers = Seller.objects.order_by('-hire_date')

    #Get MVP
    mvp_sellers = Seller.objects.all().filter(is_mvp = True)

    context = {
        'sellers' : sellers,
        'mvp_sellers' : mvp_sellers
    }
    return render(request,'/var/www/html/Sri/realestate-full-app-django-master/templates/seller/sellers.html',context)

def seller(request,seller_id):
    seller = get_object_or_404(Seller, pk=seller_id)
    context = {
        'seller' : seller
    }
    return render(request,'/var/www/html/Sri/realestate-full-app-django-master/templates/seller/seller.html',context)