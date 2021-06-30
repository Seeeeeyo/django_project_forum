from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse

from .forms import SignUpForm
from .models import User


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = SignUpForm
    success_url = '/'


class ProfileUpdateView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'avatar']
    template_name = 'registration/profil_update.html'

    def get_success_url(self):
        return reverse('profile_detail', args=(self.object.pk,))

    # def form_valid(self, form):
        # import pdb;pdb.set_trace()
        # return super().form_valid(form)


class ProfileDetailView(DetailView):
    template_name = 'registration/profil_detail.html'
    model = User
