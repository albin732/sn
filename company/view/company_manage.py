from django.shortcuts import render,redirect
from company.models import OrderStack
from django.views import View

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from common.decorators import staff_required


@method_decorator([login_required, staff_required], name='dispatch')
class OrderManagement(View):
    def post(self,request):
        template_name='company/manage.html'
        return render(request,template_name)

    def get(self,request):
        orders_manage = OrderStack.active_order()

        # pagination starts
        page = request.GET.get('page', 1)
        paginator = Paginator(orders_manage, 10)
        try:
            orders_manage = paginator.page(page)
        except PageNotAnInteger:
            orders_manage = paginator.page(1)
        except EmptyPage:
            orders_manage = paginator.page(paginator.num_pages)
        # pagination ends

        return render(request,'company/manage.html',{'orders_manage':orders_manage})