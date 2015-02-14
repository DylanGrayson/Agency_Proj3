
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class MoreInfoForm(forms.Form):
	email = forms.EmailField(label="Your email")
	name = forms.CharField(max_length=128)


def index(request):
	if request.method == 'POST':
		form = MoreInfoForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data["email"]
	else:
		return render(request, "main/index.html", {})

def splash(request):
	return render(request, "main/splash.html", {})

def about(request):
	return render(request, "main/about.html", {})

def campaign1(request):
	return render(request, "main/campaign1.html", {})

def campaign2(request):
	return render(request, "main/campaign2.html", {})

def campaign3(request):
	return render(request, "main/campaign3.html", {})


