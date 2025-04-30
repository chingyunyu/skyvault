from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from app.models.subscription import Subscription
from app.models.payment import Payment

def customer(request):
    email = request.session.get('email')
    subscriptions = Subscription.objects.all()

    # Find current valid plan
    current_plan = None
    now = timezone.now()
    payments = Payment.objects.filter(email=email)
    for p in payments:
        if p.start <= now <= p.end:
            current_plan = p.plan
            break

    return render(request, 'customer.html', {
        "subscriptions": subscriptions,
        "current_plan": current_plan,
    })

@csrf_exempt
def terminate(request):
    if request.method == 'POST':
        email = request.session.get('email')
        plan = request.POST.get('plan')
        payment = Payment.objects.filter(email=email, plan=plan).last()
        if payment:
            payment.end = timezone.now()
            payment.save()
    return redirect('/customer')