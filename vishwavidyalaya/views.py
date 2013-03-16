from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import TemplateView
from guardian.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from profiles.models import Faculty, Student


class HomeView(TemplateView):
    template_name = 'index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'
