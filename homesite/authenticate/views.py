from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.shortcuts import redirect


class MyLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        redirect_to = self.request.GET.get('next', self.success_url)
        super().form_valid(form)
        return redirect(redirect_to)


class MyLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('index')
