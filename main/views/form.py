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
	age = forms.IntegerField(label="Age")
	skin_tone = forms.CharField(label="Skin Tone", max_length=128)
	color = forms.CharField(label="Paint Color")

class VirusCon(forms.Form):
	name = forms.CharField(label="Name", max_length=128)
	age = forms.IntegerField(label="Age")
	skin_tone = forms.CharField(label="Skin Tone", max_length=128)
	color = forms.CharField(label="Paint Color")

class FriendClosure(forms.Form):
	name = forms.CharField(label="Name", max_length=128)
	age = forms.IntegerField(label="Age")
	skin_tone = forms.CharField(label="Skin Tone", max_length=128)
	color = forms.CharField(label="Paint Color")

class ThrowbackSchool(forms.Form):
	name = forms.CharField(label="Name", max_length=128)
	age = forms.IntegerField(label="Age")
	skin_tone = forms.CharField(label="Skin Tone", max_length=128)
	color = forms.CharField(label="Paint Color")
