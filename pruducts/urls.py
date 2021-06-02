from django.urls import path


from pruducts.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]