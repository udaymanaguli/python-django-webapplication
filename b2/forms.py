from django import forms
from .models import Choice


class saved(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["cidentity", "choice"]
