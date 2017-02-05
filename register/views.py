from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.forms import *


def home(request):
	form = Sign_Up_DataForm
	form1 = LoginForm
	return render(request, 'base.html', {'form': form, 'form1':form1})