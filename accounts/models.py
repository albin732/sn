from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self,user_type, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        Validation can be set here for console user creation.
        """

        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(user_type=user_type,email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,user_type, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password and Usertype through console.
        Saved through create_user
        """
        extra_fields.setdefault('staff', True)
        extra_fields.setdefault('superstaff', True)
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_admin') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(user_type,email, password, **extra_fields)




class User(AbstractBaseUser,PermissionsMixin):
    USR_TYP = (
        ('1', 'Customer'),
        ('2', 'Staff'),
        ('3', 'SuperStaff'),
        ('4', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USR_TYP, default=1)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    first_name = models.CharField(max_length=100, blank=True, null=True,)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    address = models.TextField(blank = True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=15,blank=True, null=True)  # null = True means not mandatory
    phone_2 = models.CharField(max_length=15,blank=True, null=True)
    date_joined = models.DateTimeField(default = timezone.now) #join date, single time entry
    active = models.BooleanField(default=False)  # can login
    staff = models.BooleanField(default=False)   # non super staff
    superstaff = models.BooleanField(default=False)   # super admin staff
    admin = models.BooleanField(default=False)  # superuser site admin
    timestamp = models.DateTimeField(auto_now_add=True)

    # objects = MyUserManager()

    USERNAME_FIELD = 'email'    # as username
    REQUIRED_FIELDS = ['user_type'] # for superuser creation like 'phone', 'first_name'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_user_by_email(email):
        return User.objects.get(email=email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_superstaff(self):
        "Is the user a member of sustaff?"
        return self.superstaff

    @property
    def is_admin(self):
        "Is the user a member of admin?"
        # Simplest possible answer: All admins are staff
        return self.admin

    @property
    def is_active(self):
        return self.active


# profile table models 

class UserCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_balance = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    given_discount = models.DecimalField(max_digits=7, decimal_places=2,default=0)

    def __str__(self):
        return self.user.email

    def email_id(self):
        return self.user.email




class UserStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DESIGNATION_CHOICE = (
        (1, 'MD'),
        (2, 'Marketing Manager'),
        (3, 'Accountant'),
        (4, 'Website Manager'),
        (5, 'Website Staff'),
        (6, 'Executive Chef'),
        (7, 'Sous Chef'),
        (8, 'Chef'),
        (9, 'Sales Executive'),
        (10, 'Packing Staff'),
        (11, 'Cleaning Staff'),
        (12, 'Movement Staff'),
        (13, 'Delivery Staff'),
    )
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICE, null=True)
    image = models.ImageField(upload_to='image/staff_img',null=True)
    ID_CHOICE = (
        (1, 'Driving Licence'),
        (2, 'Pasport'),
        (3, 'Adhar'),
    )
    id_card = models.CharField(max_length=50, choices=ID_CHOICE, null=True)
    id_card_image = models.ImageField(upload_to='image/staff_id',null=True)

    def __str__(self):
        return self.user.email

    def email_id(self):
        return self.user.email


class UserSuperStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length = 100,null=True)
    image = models.ImageField(upload_to='image/staff_img',null=True)
    ID_CHOICE = (
        (1, 'Driving Licence'),
        (2, 'Pasport'),
        (3, 'Adhar'),
    )
    id_card = models.CharField(max_length=10, choices=ID_CHOICE, null=True)
    id_card_image = models.ImageField(upload_to='image/staff_id',null=True)

    def __str__(self):
        return self.user.email

    def email_id(self):
        return self.user.email


class UserAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notes = models.CharField(max_length = 255,null=True)
    work_reference = models.TextField(null=True)

    def __str__(self):
        return self.user.email

    def email_id(self):
        return self.user.email


#  signals for auto create profile table 

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type == 4:
             UserAdmin.objects.create(user=instance)
        elif instance.user_type == 3:
             UserSuperStaff.objects.create(user=instance)
        elif instance.user_type == 2:
             UserStaff.objects.create(user=instance)
        elif instance.user_type == 1:
             UserCustomer.objects.create(user=instance)
        
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type == 4:
        instance.useradmin.save()       #small letters
    elif instance.user_type == 3:
        instance.ssersuperstaff.save()
    elif instance.user_type == 2:
        instance.userstaff.save()
    elif instance.user_type == 1:
        instance.usercustomer.save()


