from django import forms

from .models import Language

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = [
            "name",
            "name_in_language",
        ]
