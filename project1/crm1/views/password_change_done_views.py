from django.contrib.auth.views import PasswordContextMixin
from django.views.generic import TemplateView

class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = "crm1/password_reset_sent.html"
    title = ("Password change successful")