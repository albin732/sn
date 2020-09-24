from django.views import View
from django.shortcuts import render,redirect
from accounts.forms import CustomerRegistrationForm
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group


class CustomerRegisteration(View):

    def get(self,request):
        return render(request,'accounts/customer_registeration.html')

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_email = form.cleaned_data.get('email')

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)

            messages.success(request,'Account is created for ' + user_email)
            return redirect(reverse('accounts_ns:login'))
        else:
            # form = CustomerRegistrationForm()
            
            return render(request,'accounts/customer_registeration.html',context = {'form':form})
        return render(request,'accounts/customer_registeration.html',context = {'form':form})


