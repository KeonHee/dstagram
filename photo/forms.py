from django import forms
from photo.models import Photo


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['id', 'user', 'image_file', 'title', 'contents', ]
