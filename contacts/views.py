from django.contrib import messages
from .models import Contact
from django.shortcuts import render, redirect
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
         listing_id = request.POST['listing_id']
         listing = request.POST['listing']
         name = request.POST['name']
         email = request.POST['email']
         phone = request.POST['phone']
         message = request.POST['message']
         user_id = request.POST['user_id']
         realotr_email = request.POST['realtor_email']

          #check if use has made iquire
         if request.user.is_authenticated:
              user_id = request.user.id
              has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
              if has_contacted:
                  messages.error(request, 'You have already mad an inquiry for this list')
                  return redirect('/listing/+listing_id')

         contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                      phone=phone, message=message, user_id=user_id)
         contact.save()

          #send email
         send_mail(
              'property Listing Inquiry'
              'There has been an inquire for ' + listing + '. Sign into the admin panel for more',
              'tatisopova@gmail.com'
              [realotr_email, 'tatisopvoa@gmail.com'],
              fail_silently = False
         )
         messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
         return redirect('/listing/+listing_id')