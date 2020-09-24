from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from ..models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Login(View):
    return_url = None
    
    def get(self,request):
        if not request.user.is_authenticated:
            Login.return_url = request.GET.get('return_url')
            return render(request,'accounts/login.html')
        else:
            userobj = User.get_user_by_email(request.session.get('email'))
            if userobj.user_type == '1':
                return redirect('stores_ns:home')
            elif userobj.user_type == '2' and userobj.is_staff:
                return redirect('company_ns:staff_dashboard')
            elif userobj.user_type == '3' and userobj.is_superstaff:
                return redirect('company_ns:super_staff_dashboard')
            elif userobj.user_type == '4' and userobj.is_admin:
                return redirect('company_ns:admin_dashboard')
            else:
                return redirect('stores_ns:home')

    def post(self,request):
        # form = AuthenticationForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        userobj = User.get_user_by_email(email)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = userobj.id
                request.session['email'] = userobj.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    if userobj.user_type == '1':
                        return redirect('stores_ns:home')
                    elif userobj.user_type == '2' and userobj.is_staff:
                        return redirect('company_ns:staff_dashboard')
                    elif userobj.user_type == '3' and userobj.is_superstaff:
                        return redirect('company_ns:super_staff_dashboard')
                    elif userobj.user_type == '4' and userobj.is_admin:
                        return redirect('company_ns:admin_dashboard')
                    else:
                        return redirect('stores_ns:home')

        else:
            messages.info(request,'Email or Password is Incorrect')
            return redirect('accounts_ns:login')


@method_decorator([login_required],name='dispatch')
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('stores_ns:home')