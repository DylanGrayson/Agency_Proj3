from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from main.models import Campaign


class MoreInfoForm(forms.Form):
    email = forms.EmailField(label="Your email")
    name = forms.CharField(max_length=128)


class FreeFacepaint(forms.Form):
    name = forms.CharField(label="Name", max_length=128)
    age = forms.IntegerField(label="Age")
    skin_tone = forms.CharField(label="Skin Tone", max_length=128)
    color = forms.CharField(label="Paint Color")


class MiceBorrow(forms.Form):
    name = forms.CharField(label="Name", max_length=128)
    city = forms.CharField(label="City", max_length=128)
    num_mice = forms.CharField(label="Number of Mice", max_length=128)


class VirusCon(forms.Form):
    name = forms.CharField(label="Name", max_length=128)
    email = forms.EmailField(label="Age")


class FriendClosure(forms.Form):
    name = forms.CharField(label="Name", max_length=128)
    age = forms.IntegerField(label="Age")
    city = forms.CharField(label="City", max_length=128)
    state = forms.CharField(label="State", max_length=128)


class ThrowbackSchool(forms.Form):
    name = forms.CharField(label="Name", max_length=128)
    age = forms.IntegerField(label="Age")
    school = forms.CharField(label="School", max_length=128)
