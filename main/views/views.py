from django.shortcuts import render
from django.http import HttpResponse
from main.models import Campaign
from main.views.form import MoreInfoForm, FreeFacepaint, MiceBorrow, VirusCon, FriendClosure, ThrowbackSchool


def splash(request):
    return render(request, "main/splash.html", {})


def about(request):
    return render(request, "main/about.html", {})


def blue_man(request):
    if request.method == 'POST':
        form = FreeFacepaint(request.POST)
        if form.is_valid():
            age = form.cleaned_data["age"]
            skin_tone = form.cleaned_data["skin_tone"]
            name = form.cleaned_data["name"]
            color = form.cleaned_data["color"]
            return render(request, "main/form_blue.html", {'data': form.cleaned_data, 'campaign': 'blue_man'})
    else:
        return render(request, "main/form.html", {'form': FreeFacepaint})


def dont_care(request):
    if request.method == 'POST':
        form = MoreInfoForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            return render(request, "main/form_care.html", {'data': form.cleaned_data, 'campaign': 'dont_care'})
    else:
        return render(request, "main/form.html", {'form': MoreInfoForm})

def mouse(request):
    if request.method == 'POST':
        form = MiceBorrow(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            mice_num = form.cleaned_data["num_mice"]
            name = form.cleaned_data["name"]
            return render(request, "main/form_mice.html", {'data': form.cleaned_data, 'campaign': 'dont_care'})
    else:
        return render(request, "main/form.html", {'form': MoreInfoForm})

def friend(request):
    if request.method == 'POST':
        form = VirusCon(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            return render(request, "main/form_friend.html", {'data': form.cleaned_data, 'campaign': 'dont_care'})
    else:
        return render(request, "main/form.html", {'form': MoreInfoForm})

def closure(request):
    if request.method == 'POST':
        form = FriendClosure(request.POST)
        if form.is_valid():
            age = form.cleaned_data["age"]
            name = form.cleaned_data["name"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            return render(request, "main/form_closure.html", {'data': form.cleaned_data, 'campaign': 'dont_care'})
    else:
        return render(request, "main/form.html", {'form': MoreInfoForm})

def old_school(request):
    if request.method == 'POST':
        form = ThrowbackSchool(request.POST)
        if form.is_valid():
            age = form.cleaned_data["age"]
            name = form.cleaned_data["name"]
            school = form.cleaned_data["school"]
            return render(request, "main/form_throwback.html", {'data': form.cleaned_data, 'campaign': 'dont_care'})
    else:
        return render(request, "main/form.html", {'form': MoreInfoForm})


def campaigns(request):
    return render(request, "main/campaigns.html", {'campaigns': Campaign.objects.all()})
