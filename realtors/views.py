from django.shortcuts import render

# Create your views here.
def seller(request):
     #Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    mvp_realtors = Realtor.objects.get().filter(name)

    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors
    }
    return render(request,'realtors/seller.html', context)
