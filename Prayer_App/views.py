from django.shortcuts import render
from .models import PrayerTopic, Video
from django.shortcuts import render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings

def homepage(request):
    # Add church information here
    return render(request, 'homepage.html')

def prayers(request):
    prayer_topics = PrayerTopic.objects.all()
    return render(request, 'prayers.html', {'prayer_topics': prayer_topics})

def videos(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'video_urls': videos})

def donation(request):
    return render(request, 'donation.html')
def process_donation(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': amount,
            'item_name': 'Donation',
            'currency_code': 'USD',
            'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
            'return_url': request.build_absolute_uri(reverse('donation_success')),
            'cancel_return': request.build_absolute_uri(reverse('donation_cancel')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'checkout.html', {'form': form})
    else:
        return redirect('donation.html')

def donation_success(request):
    # Handle successful payment
    return render(request, 'donation_success.html')

def donation_cancel(request):
    # Handle payment cancellation
    return render(request, 'donation_cancel.html')
