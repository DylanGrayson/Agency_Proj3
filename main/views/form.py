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



