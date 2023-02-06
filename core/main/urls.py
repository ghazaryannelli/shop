from django.urls import path
from .views import HomeListView, AboutListView, ProductsListView, ContactListView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about/', AboutListView.as_view(), name='about'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('contact', ContactListView.as_view(), name='contact'),

]