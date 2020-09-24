from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import messages

# from .models import UserCustomerProfile
# User = get_user_model()
from .models import User


class UserAdminCreationForm(forms.ModelForm):
    pass


class UserAdminChangeForm(forms.ModelForm):
    pass


class CustomerProfileForm(forms.ModelForm):
    pass


class CustomerRegistrationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'gender',
                  'address', 'city', 'state', 'pin_code', 'phone', 'phone_2')

    def clean_email(self):
        email_passed = self.cleaned_data.get('email')
        email_req = User.objects.filter(email=email_passed)
        print(email_req)
        if email_req:
            raise forms.ValidationError('Email already registered')
        # return render(request,'accounts/customer_register.html')
        return email_passed

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesn't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CustomerRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # send confirmation email and make it true,, by default it must be false
        user.active = True
        user.staff = False
        user.superstaff = False
        user.admin = False
        user.user_type = '1'
        if commit:
            user.save()
        return user


class StaffRegistrationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User  # required for the form
        fields = ('email', 'first_name', 'last_name', 'gender',
                  'address', 'city', 'state', 'pin_code', 'phone', 'phone_2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StaffRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # send confirmation email and make it true,, by default it must be false
        user.active = False
        user.staff = True
        user.superstaff = False
        user.admin = False
        user.user_type = '2'
        if commit:
            user.save()
        return user


class SuperStaffRegistrationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User  # required for the form
        fields = ('email', 'first_name', 'last_name', 'gender',
                  'address', 'city', 'state', 'pin_code', 'phone', 'phone_2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SuperStaffRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # send confirmation email and make it true,, by default it must be false
        user.active = False
        user.staff = True
        user.superstaff = True
        user.admin = False
        user.user_type = '3'
        if commit:
            user.save()
        return user
