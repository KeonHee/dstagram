from django import forms
from photo.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['user', 'image_file', 'title', 'contents']
