from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME



# checks authentication
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            # userobj = User.get_user_by_email(request.session.get('email'))
            # if userobj.user_type == '1':
            #     return redirect('stores_ns:home')
            # elif userobj.user_type == '2' and userobj.is_staff:
            #     return redirect('company_ns:staff_dashboard')
            # elif userobj.user_type == '3' and userobj.is_superstaff:
            #     return redirect('company_ns:super_staff_dashboard')
            # elif userobj.user_type == '4' and userobj.is_admin:
            #     return redirect('company_ns:admin_dashboard')
            # else:
            return redirect('stores_ns:home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

# for groups and roles
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            return view_func(request,*args,**kwargs)
        return wrapper_func
    return decorator


# for function based
# from common.decorators import staff_required
# @staff_required
def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/login'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/accounts/err_404'):
    '''
    Decorator for views that checks that the logged in user is a student,
    redirects to the log-in page if necessary.
    '''
    
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator