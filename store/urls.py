from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Index
from .view.checkout import CheckOut
from .view.orders import Orders
from .view.payment import Payment
from .middlewares.auth import auth_middleware

urlpatterns = [
    # path('',views.home_page,name='home'),
    path('home/',Index.as_view(),name='home'),
    path('product/',views.product_page,name='products'),
    path('productdetails/<int:pk>',views.productdetails_page,name='productdetails'),
    path('productdetails/',views.productdetails_page,name='productdetails'),
    path('cart/',views.cart_page,name='cart'),
    path('aboutus/',views.aboutus_page,name='aboutus'),
    path('contact/',views.contact_page,name='contact'),
    path('check-out/',CheckOut.as_view(),name='check-out'),
    path('orders/',Orders.as_view(),name='orders'),
    path('payment/',Payment.as_view(),name='payment'),

    # path('check-out/',views.checkout_page,name='check-out'),


    path('test/',views.test_page,name='test')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)