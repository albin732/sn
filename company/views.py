from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.decorators import staff_required

# Create your views here.


def staffdashboard(request):
    template_name='company/staff_dashboard.html'
    return render(request,template_name)


def superstaffdashboard(request):
    template_name='company/superstaff_dashboard.html'
    return render(request,template_name)
    

def admindashboard(request):
    template_name='company/admin_dashboard.html'
    return render(request,template_name)


def analysis(request):
    template_name='company/analysis.html'
    return render(request,template_name)

def inventory(request):
    template_name='company/inventory.html'
    return render(request,template_name)


def settings(request):
    template_name='company/settings.html'
    return render(request,template_name)

def support(request):
    template_name='company/support.html'
    return render(request,template_name)