from django.shortcuts import render,get_object_or_404
from sellers.models import Seller, Rating


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
    if request.method == "POST":
        #  user_id = request.user.id
        name = request.POST['name']
        # stars = request.POST.get('stars', '') 
        message = request.POST['message'] 
        sellerid = seller_id

        query = Rating(message = message, name = name )
        query.sellerid_id = sellerid
        # query.stars = stars
        query.save()
    seller = get_object_or_404(Seller, pk=seller_id)
    rating = Rating.objects.all().filter(sellerid = seller_id)

    context = {
        'seller' : seller,
        'ratings':rating
    }
    return render(request,'/var/www/html/Sri/realestate-full-app-django-master/templates/seller/seller.html',context)

   