from django.urls import path
from app.views.index import index
from app.views.admin import admin
from app.views.customer import customer, terminate
from app.views.payment import payment
from app.views import api

urlpatterns = [
    path('', index),
    path('admin', admin),
    path('customer', customer),
    path('terminate', terminate),
    path('payment', payment),
    path('api/payments/', api.payments),                # handles GET (list) and POST (create)
    path('api/payments/<int:id>/', api.payment_detail), # handles GET (detail), PUT, DELETE
]