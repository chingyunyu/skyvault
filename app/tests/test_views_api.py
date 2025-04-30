import pytest
import json
from app.models.payment import Payment
from django.utils import timezone
from datetime import timedelta

@pytest.mark.django_db
class TestPaymentAPI:

    def test_create_payment(self, client):
        payload = {
            'email': 'create@skyvault.com',
            'plan': 'basic',
            'price': 300
        }
        response = client.post('/api/payments/', data=json.dumps(payload), content_type='application/json')
        assert response.status_code == 201
        data = response.json()
        assert data['email'] == 'create@skyvault.com'
        assert data['plan'] == 'basic'
        assert data['price'] == 300
        assert 'start' in data
        assert 'end' in data

    def test_list_payments(self, client):
        now = timezone.now()
        Payment.objects.create(email='list1@skyvault.com', plan='basic', price=300, start=now, end=now + timedelta(days=30))
        Payment.objects.create(email='list2@skyvault.com', plan='professional', price=600, start=now, end=now + timedelta(days=30))
        Payment.objects.create(email='list3@skyvault.com', plan='enterprise', price=1200, start=now, end=now + timedelta(days=30))

        response = client.get('/api/payments/')
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 3  # Could be more if other tests inserted
        for item in data:
            assert 'email' in item
            assert 'plan' in item
            assert 'price' in item
            assert 'start' in item
            assert 'end' in item

    def test_get_payment_detail(self, client):
        now = timezone.now()
        payment = Payment.objects.create(email='get@skyvault.com', plan='basic', price=300, start=now, end=now + timedelta(days=30))

        response = client.get(f'/api/payments/{payment.id}/')
        assert response.status_code == 200
        data = response.json()
        assert data['email'] == 'get@skyvault.com'
        assert data['plan'] == 'basic'
        assert data['price'] == 300
        assert 'start' in data
        assert 'end' in data

    def test_update_payment(self, client):
        now = timezone.now()
        payment = Payment.objects.create(email='update@skyvault.com', plan='basic', price=300, start=now, end=now + timedelta(days=30))

        payload = {
            'email': 'update@skyvault.com',
            'plan': 'professional',
            'price': 600
        }
        response = client.put(f'/api/payments/{payment.id}/', data=json.dumps(payload), content_type='application/json')
        assert response.status_code == 200
        data = response.json()
        assert data['email'] == 'update@skyvault.com'
        assert data['plan'] == 'professional'
        assert data['price'] == 600
        assert 'start' in data
        assert 'end' in data

    def test_delete_payment(self, client):
        now = timezone.now()
        payment = Payment.objects.create(email='delete@example.com', plan='basic', price=300, start=now, end=now + timedelta(days=30))

        response = client.delete(f'/api/payments/{payment.id}/')
        assert response.status_code == 200
        data = response.json()
        assert data['message'] == 'Payment deleted'

        # Confirm it was actually deleted
        assert not Payment.objects.filter(id=payment.id).exists()

    def test_get_nonexistent_payment(self, client):
        response = client.get('/api/payments/99999/')
        assert response.status_code == 404

    def test_method_not_allowed(self, client):
        payload = {}
        response = client.put('/api/payments/', data=json.dumps(payload), content_type='application/json')
        assert response.status_code == 405