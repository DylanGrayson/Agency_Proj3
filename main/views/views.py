from django.shortcuts import render
from django.http import HttpResponse
from main.models import Campaign

def splash(request):
	return render(request, "main/splash.html", {})

def about(request):
	return render(request, "main/about.html", {})

def campaigns(request):
	return render(request, "main/campaigns.html", {'campaigns': Campaign.objects.all()})