from django.shortcuts import render
from django.http import HttpResponse
from main.models import Campaign
from main.views.form import MoreInfoForm, FreeFacepaint

def splash(request):
	return render(request, "main/splash.html", {})

def about(request):
	return render(request, "main/about.html", {})

def blue_man(request):
	if request.method == 'POST':
		form = FreeFacepaint(request.POST)
		if form.is_valid():
			age = form.cleaned_data["age"]
			color = form.cleaned_data["color"]
			return render(request, "main/thankyou.html", {'data': form.cleaned_data, 'campaign': 'blue_man'})
	else:
		return render(request, "main/form.html", { 'form': FreeFacepaint })

def dont_care(request):
	if request.method == 'POST':
		form = MoreInfoForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data["email"]
			name = form.cleaned_data["name"]
			return render(request, "main/thankyou.html", {'data': form.cleaned_data, 'campaign': 'dont_care'})
	else:
		return render(request, "main/form.html", { 'form': MoreInfoForm })

def campaigns(request):
	return render(request, "main/campaigns.html", {'campaigns': Campaign.objects.all()})
