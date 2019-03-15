from django import forms
from .models import CV

class DocumentForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ('name', 'document', )