import pytest
from app.models.payment import Payment
from django.utils import timezone
from datetime import timedelta

@pytest.mark.django_db
class TestPaymentModel:

    def test_create_payment(self):
        now = timezone.now()
        payment = Payment.objects.create(
            email='create@skyvault.com',
            plan='basic',
            price=300,
            start=now,
            end=now + timedelta(days=30)
        )
        assert payment.email == 'create@skyvault.com'
        assert payment.plan == 'basic'
        assert payment.price == 300
        # Allow slight difference in timestamps if needed
        assert abs((payment.start - now).total_seconds()) < 1
        assert abs((payment.end - (now + timedelta(days=30))).total_seconds()) < 1

    def test_terminate_payment(self):
        now = timezone.now()

        # Always create a fresh payment
        payment = Payment.objects.create(
            email='terminate@skyvault.com',
            plan='basic',
            price=300,
            start=now,
            end=now + timedelta(days=30)
        )

        # Terminate the payment
        new_end_time = timezone.now()
        payment.end = new_end_time
        payment.save()

        payment.refresh_from_db()
        # Allow slight timing difference
        assert abs((payment.end - new_end_time).total_seconds()) < 1