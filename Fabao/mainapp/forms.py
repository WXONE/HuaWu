from django import forms
from mainapp.models import UploadFile
from django.forms import Form,ModelForm

class UploadFileForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = UploadFile
        fields = '__all__'