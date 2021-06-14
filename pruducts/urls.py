from django.urls import path

app_name = 'pruducts'

from pruducts.views import products

urlpatterns = [

from pruducts.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]