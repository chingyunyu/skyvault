from django.shortcuts import render, redirect
from django.utils import timezone
from app.models.subscription import Subscription
from app.models.payment import Payment
from datetime import timedelta


def payment(request):
    email = request.session.get('email')
    if request.method == 'GET':
        plan = request.GET.get('plan')
        sub = Subscription.objects.get(plan=plan)
        return render(request, 'payment.html', {"plan": plan, "price": sub.price})

    if request.method == 'POST':
        plan = request.POST.get('plan')
        price = request.POST.get('price')

        # Create a payment record
        now = timezone.now()
        Payment.objects.create(
            email=email,
            plan=plan,
            price=price,
            start=now,
            end=now + timedelta(days=30)
        )
        return redirect('/customer')