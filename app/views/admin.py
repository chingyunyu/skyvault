from django.shortcuts import render, redirect
from app.models.account import Account
from app.models.subscription import Subscription

def admin(request):
    if request.method == 'POST':
        plan = request.POST.get('plan')
        price = request.POST.get('price')
        Subscription.objects.create(plan=plan, price=price)
    
    accounts = Account.objects.all()
    subscriptions = Subscription.objects.all()
    return render(request, 'admin.html', {"accounts": accounts, "subscriptions": subscriptions})