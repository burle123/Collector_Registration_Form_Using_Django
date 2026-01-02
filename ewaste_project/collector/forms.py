from django import forms
from .models import Collector

class CollectorForm(forms.ModelForm):
    class Meta:
        model = Collector
        fields = '__all__'
