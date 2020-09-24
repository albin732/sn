from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,UserCustomer,UserStaff,UserSuperStaff,UserAdmin
# Register your models here.

# User = get_user_model()
class AdminUser(BaseUserAdmin):
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    class Meta:
        model = User
        fields = '__all__'
    
    list_display = ('user_type','email','first_name','last_name','phone','date_joined', 'staff','superstaff', 'admin', 'active')   # viewed at Select user to change in dj
    list_filter = ('admin', 'staff','superstaff', 'active')
    fieldsets = (
        (None, {'fields': ('user_type','email', 'password')}),    # shown at dj change user page,, none or title
        ('personal info', {'fields':('first_name','last_name','gender', 'address','city','state','pin_code', 'phone','phone_2')}),    # shown at dj change user page under personal info
        ('Active Permissions', {'fields': ('admin', 'staff','superstaff', 'active')}), #   shown at dj change user page under Permissions
        # ('Groups', {'fields': ('groups',)}),
        # ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_type','email', 'password1', 'password2','first_name','last_name','gender', 'address','city','state','pin_code', 'phone','phone_2')}  # add new user @dj
        ),
        ('Active Permissions', {'fields': ( 'staff','superstaff', 'active',)}),
        # ('Groups', {'fields': ('groups',)}),
        # ('Permissions', {'fields': ('user_permissions',)}),
    )
    search_fields = ('email','first_name','last_name','phone','phone_2')
    ordering = ('user_type','-active','-admin','-staff','-superstaff')
    filter_horizontal = ()



class AdminUserCustomer(admin.ModelAdmin):
    list_display = ('email_id','card_balance','given_discount')

class AdminUserStaff(admin.ModelAdmin):
    list_display = ('email_id','designation','image','id_card','id_card_image')

class AdminUserSuperStaff(admin.ModelAdmin):
    list_display = ('email_id','designation','image','id_card','id_card_image')

class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('email_id','notes','work_reference')




admin.site.register(User,AdminUser)
admin.site.register(UserCustomer,AdminUserCustomer)
admin.site.register(UserStaff,AdminUserStaff)
admin.site.register(UserSuperStaff,AdminUserSuperStaff)
admin.site.register(UserAdmin,AdminUserAdmin)

