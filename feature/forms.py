from django import forms
from .models import Feature

class DateInput(forms.DateInput):
    input_type = 'date'

class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description', 'target_date', 'product_area','client', 'feat_priority',)
        widgets = {
            'target_date': DateInput(),
        }