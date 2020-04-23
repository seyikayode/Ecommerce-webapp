from django.urls import path
from .views import HomeView, ProductView, add_to_cart, remove_from_cart, OrderSummary, add_single_item_to_cart,\
    remove_single_item_from_cart, CheckOutView, PaymentView, AddCoupon, RefundView, SearchView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ProductView.as_view(), name='product'),
    path('order-summary/', OrderSummary.as_view(), name='order-summary'),
    path('checkout/', CheckOutView.as_view(), name='check-out'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCoupon.as_view(), name='add-coupon'),
    path('request-refund/', RefundView.as_view(), name='request-refund'),
    path('search-results/', SearchView.as_view(), name='search'),
    path('add/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('add/item/<slug>/', add_single_item_to_cart, name='add-single-item-to-cart'),
    path('remove/item/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart')
]
