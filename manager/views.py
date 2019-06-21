from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import View

from accounts.utils import pretty_request
from .forms import MenuForm


class IndexView(TemplateView):
	template_name = 'manager/index.html'

	def get(self, request, *args, **kwargs):
		return super(self.__class__, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		pass


class HomepageView(TemplateView):
	template_name = 'manager/manager_profile.html'

	def get(self, request, *args, **kwargs):
		return super(self.__class__, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		pass