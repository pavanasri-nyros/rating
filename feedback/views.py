from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Feedback

def feedback(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        stars = request.POST['stars']


        # Check if user has made inquiry already:
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Feedback.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already gave the feedback to the realtor ')
                return redirect('/listings/'+listing_id)

        contact = Feedback(listing_id=listing_id, stars = stars, name=name, email=email, phone=phone, message=message, user_id=user_id )
        contact.save()

        # SEND EMAIL
        send_mail(
            'Property Listing Inquiry',
            'There has been an feedback for  realtor . Sign in to the admin panel for more information.',
            'pavanasri.nyros@gmail.com',
            [realtor_email, 'paripalepu@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)