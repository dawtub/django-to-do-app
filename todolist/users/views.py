from django.contrib.auth import views
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomLoginForm, CustomUserCreationForm


class CustomLoginView(views.LoginView):
    form_class = CustomLoginForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'registration/signup.html'
