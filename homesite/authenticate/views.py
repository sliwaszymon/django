from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import LoginForm, RegistrationForm
from django.shortcuts import redirect


class MyLoginView(LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm
    success_url = 'index'

    def form_valid(self, form):
        redirect_to = self.request.GET.get('next', self.success_url)
        super().form_valid(form)
        return redirect(redirect_to)


class MyLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('index')


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegistrationForm()
        return context

    def post(self, request, *args, **kwargs):
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse_lazy('login'))
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

# TODO: password reset and change own views
