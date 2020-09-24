
from django.urls import path
from . import views
from .view.logs import Login, Logout
from .view.register import CustomerRegisteration

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('customer_registeration/',CustomerRegisteration.as_view(),name='customer_registeration'),
    path('profile/',views.view_profile,name='profile'),
    path('user_profile/',views.profile,name='user_profile'),
    path('create_new_user/',views.create_new_user,name='create_new_user'),
    path('err_404/',views.err_404_page,name='err_404'),


    # path('test/',views.test_page,name='test')
]