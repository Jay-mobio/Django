from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.http import url_has_allowed_host_and_scheme
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, resolve_url
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.views.generic.edit import FormView





class LoginView(FormView):
    """
    Display the login form and handle the login action.
    """

    form_class = AuthenticationForm
    authentication_form = None
    next_page = None
    redirect_field_name = "/crm1/user.html"
    template_name = "crm1/login.html"
    redirect_authenticated_user = False
    extra_context = None
    get_success_url = "/crm1/user.html"

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name, self.request.GET.get(self.redirect_field_name, "")
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ""

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update(
            {
                self.redirect_field_name: self.get_redirect_url(),
                "site": current_site,
                "site_name": current_site.name,
                **(self.extra_context or {}),
            }
        )
        return context