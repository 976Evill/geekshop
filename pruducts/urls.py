from django.urls import path
app_name = 'pruducts'

from pruducts.views import products

urlpatterns = [

    path('', products, name='index'),
]