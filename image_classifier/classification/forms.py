from django import forms
from classification.models import UploadedImage

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
