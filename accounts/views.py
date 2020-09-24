from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
# from .models import User 
from .models import User

from django.contrib.auth.decorators import login_required


# Create your views here.






# def register_page(request):
#     if request.method == 'POST':
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             print('###########valid reg')
#             form.save()
#             user = form.cleaned_data.get('username')
#             print('###########clean')
#            # return redirect(reverse('home:home'))
#             messages.success(request,'Account was created')
#             return redirect(reverse('accounts_ns:login'))
#         else:
#             messages.error(request,'Existing email or invalid password')
#             return redirect(reverse('accounts_ns:customer_registeration'))
#     else:
#         form = CustomerRegistrationForm()

#         args = {'form': form}
#         return render(request,'accounts/register.html',args)



@login_required
def view_profile(request):
    args = {'user':request.user}
    return render(request,'accounts/profile.html',args)



def profile(request):
    template_name='accounts/user_profile.html'
    return render(request,template_name)


def create_new_user(request):
    template_name='accounts/create_new_user.html'
    return render(request,template_name)


def err_404_page(request):
    template_name='err_404.html'
    return render(request,template_name)