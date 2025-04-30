from django.urls import path
from app.views.index import index
from app.views.admin import admin
from app.views.customer import customer, terminate
from app.views.payment import payment

urlpatterns = [
    path('', index),
    path('admin', admin),
    path('customer', customer),
    path('terminate', terminate),
    path('payment', payment),
]