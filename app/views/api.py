import json
from app.models.payment import Payment
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

@csrf_exempt
def payments(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        data = [
            {
                'id': p.id,
                'email': p.email,
                'plan': p.plan,
                'price': p.price,
                'start': p.start.isoformat() if p.start else None,
                'end': p.end.isoformat() if p.end else None
            }
            for p in payments
        ]
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        plan = data.get('plan')
        price = data.get('price')

        now = timezone.now()
        payment = Payment.objects.create(
            email=email,
            plan=plan,
            price=price,
            start=now,
            end=now + timedelta(days=30)
        )
        return JsonResponse({
            'id': payment.id,
            'email': payment.email,
            'plan': payment.plan,
            'price': payment.price,
            'start': payment.start.isoformat(),
            'end': payment.end.isoformat()
        }, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def payment_detail(request, id):
    try:
        payment = Payment.objects.get(pk=id)
    except Payment.DoesNotExist:
        return JsonResponse({'error': 'Payment not found'}, status=404)

    if request.method == 'GET':
        data = {
            'id': payment.id,
            'email': payment.email,
            'plan': payment.plan,
            'price': payment.price,
            'start': payment.start.isoformat() if payment.start else None,
            'end': payment.end.isoformat() if payment.end else None
        }
        return JsonResponse(data)

    if request.method == 'PUT':
        data = json.loads(request.body)
        payment.email = data.get('email', payment.email)
        payment.plan = data.get('plan', payment.plan)
        payment.price = data.get('price', payment.price)

        now = timezone.now()
        payment.start = now
        payment.end = now + timedelta(days=30)
        payment.save()

        return JsonResponse({
            'id': payment.id,
            'email': payment.email,
            'plan': payment.plan,
            'price': payment.price,
            'start': payment.start.isoformat(),
            'end': payment.end.isoformat()
        })

    if request.method == 'DELETE':
        payment.delete()
        return JsonResponse({'message': 'Payment deleted'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)