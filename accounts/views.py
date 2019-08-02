from django.shortcuts import render
from django.views.generic import DetailView

from accounts.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "registration/profile_detail.html"
    context_object_name = "profile"
