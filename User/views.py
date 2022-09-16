from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as django_login, logout as django_logout
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from User.forms import LoginForm, RegistrationForm
from User.task import send_confirmation_mail
from User.tokens import account_activation_token
from django.contrib.auth.views import PasswordChangeView
from User.forms import PasswordChangingForm

User = get_user_model()

class CustomLoginView(LoginView):
    template_name ='login.html'
    form_class = LoginForm
    success_url = reverse_lazy('list')
   
class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        result = super().form_valid(form)
        send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
        return result


def logout_page(request):
    django_logout(request)
    messages.add_message(request, messages.SUCCESS, 'Log out oldunuz!')
    return redirect(reverse_lazy('login'))


class ActiveAccountView(View):

    def get(self, request, *args, **kwargs):
        uidb64  =  kwargs ['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except ( TypeError , ValueError , OverflowError , User . DoesNotExist ):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user . save ()
            messages.success(request, 'Your account activated!')
            return redirect(reverse_lazy('login'))
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect(reverse_lazy('login'))


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request,'password_success.html')
