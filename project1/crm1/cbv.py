from msilib.schema import ListView
from turtle import title
from django.shortcuts import render,redirect

from django.views.generic.base import TemplateView

from crm1 import forms
from .models import *
from django.contrib.auth import forms
from .forms import CustomerForm, OrderForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.forms import inlineformset_factory
from django.contrib.auth.views import *
from django.views.generic.edit import FormView
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.shortcuts import render, resolve_url
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.sites.shortcuts import get_current_site




class RegisterPage(TemplateView):

    def registerUser(request):
        if request.user.is_authenticated:
            return redirect('crm1:login ')
        else:
            form = CreateUserForm()
            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    # group = Group.objects.get(name='customer')
                    # user.groups.add(group)
                    messages.success(request, 'Account was created for' +username)
                    return redirect('crm1:login')

        context = {'form':form}
        return render(request,'crm1/register.html',context)

class LogoutUser(TemplateView):
    def get(request):
        logout(request)
        return redirect('crm1:login')
    

class UserPageView:
    def userPage(request):
        print('ORDERS:', orders)
        orders = request.user.customer.order_set.all()
        context = {'orders':orders}
        return render(request, 'crm1/user.html',context)

class accountSettings:
    def ac_setings(request):
        customer = request.user.customer
        form = CustomerForm(instance=customer)
        if request.method == 'POST':
           form = CustomerForm(request.POST, request.FILES,instance=customer)
           if form.is_valid():
            form.save()    
        context = {'form':form}
        return render(request,'crm1/crm1_settings.html',context)

class ProductPage:
    def products(request):
        products = Products.objects.all()
        return render(request,'crm1/products.html',{'products':products})

class CustomerPage:
    def customer(request,pk):
        customer = Customer.objects.get(id=pk)
        orders = customer.order_set.all()
        order_count = orders.count()
        context = {'customer':customer,'orders':orders,'order_count':order_count}
        return render(request,'crm1/customer.html',context)

class CreateOrderPage:
    def createOrder(request,pk):
        OrderFormSet = inlineformset_factory(Customer,Order,fields=('products','status',),extra=10)
        customer = Customer.objects.get(id=pk)
        # formset = OrderFormSet(request.POST,instance=customer)
        formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
        # form = OrderForm(initial={'customer':customer})
        if request.method == 'POST':
            # form = OrderForm(request.POST)
            formset = OrderFormSet(request.POST, instance=customer)
            if formset.is_valid():
                formset.save()
                return redirect('/')
        context = {'formset':formset}
        return render(request,'crm1/order_form.html',context)

class UpdateOrderPage:
    def updateOrder(request,pk):

        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)
        if request.method == 'POST':
            form = OrderForm(request.POST,instance=order)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form':form}

        return render(request,'crm1/order_form.html',context)

# @allowed_users(allowed_roles=['admin'])
class DeleteOrderPage:
    def deleteOrder(request,pk):
        order = Order.objects.get(id=pk)
        if request.method == "POST":
            order.delete()
            return redirect('/')
        context = {'item':order}
        return render(request,'crm1/delete.html',context)

class PasswordResetView(PasswordContextMixin,FormView):
    email_template_name = "crm1/password_reset_email.html"
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    # subject_template_name = "crm1/password_reset_subject.txt"
    success_url = '/password_reset/sent/'
    template_name = "crm1/password_reset_form.html"
    title = ("Password reset")
    token_generator = default_token_generator


    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            # "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)

class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "crm1/password_reset_sent.html"
    title = ("Password change successful")


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = "/reset_password_complete/"
    template_name = "crm1/password_reset_form.html"
    title = ("Enter new password")
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": ("Password reset unsuccessful"),
                    "validlink": False,
                }
            )
        return context

class PasswordResetCompleteView(PasswordContextMixin, TemplateView):
    template_name = "crm1/password_reset_complete.html"
    title = ("Password reset complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = resolve_url(settings.LOGIN_URL)
        return context



class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """

    next_page = None
    redirect_field_name = "crm1/login.html"
    template_name = "crm1/login.html"
    extra_context = None

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

    def get_next_page(self):
        if self.next_page is not None:
            next_page = resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            next_page = resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            next_page = self.next_page

        if (
            self.redirect_field_name in self.request.POST
            or self.redirect_field_name in self.request.GET
        ):
            next_page = self.request.POST.get(
                self.redirect_field_name, self.request.GET.get(self.redirect_field_name)
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_page,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            # Security check -- Ensure the user-originating redirection URL is
            # safe.
            if not url_is_safe:
                next_page = self.request.path
        return next_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                "site": current_site,
                "site_name": current_site.name,
                "title": ("Logged out"),
                **(self.extra_context or {}),
            }
        )
        return context