from django import forms
from .models import Gallery, GalleryImage
from multiupload.fields import MultiFileField


class GalleryForm(forms.ModelForm):
    images = MultiFileField(required=False)

    class Meta:
        model = Gallery
        fields = []

    def save(self, commit=True):
        instance = super().save(commit)

        if self.cleaned_data.get("images"):
            for img in self.cleaned_data["images"]:
                GalleryImage.objects.create(gallery=instance, image=img)

        return instance