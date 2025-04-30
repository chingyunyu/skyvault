from django.shortcuts import render
from app.models.subscription import Subscription

def customer(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'customer.html', {"subscriptions": subscriptions})