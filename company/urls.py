from django.urls import path
from .import views
from company.view import company_manage


urlpatterns = [
    path('staff_dashboard/',views.staffdashboard,name='staff_dashboard'),
    path('super_staff_dashboard/',views.superstaffdashboard,name='super_staff_dashboard'),
    path('admin_dashboard/',views.admindashboard,name='admin_dashboard'),
    path('analysis/',views.analysis,name='analysis'),
    path('inventory/',views.inventory,name='inventory'),
    path('settings/',views.settings,name='settings'),
    path('support/',views.support,name='support'),
    path('order_management/',company_manage.OrderManagement.as_view(), name='order_management')
]