from django.contrib import admin
from .models import Sermon, Event, Gallery, GalleryImage, ContactMessage
from multiupload.fields import MultiFileField
from django.urls import reverse
from django.utils.html import format_html
from .forms import GalleryForm

admin.site.register(Sermon)
admin.site.register(Event)

# class GalleryImageInline(admin.TabularInline):
#     model = GalleryImage
#     extra = 1


# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     def get_form(self, request, obj=None, **kwargs):
#         from django import forms

#         class GalleryForm(forms.ModelForm):
#             images = MultiFileField()

#             class Meta:
#                 model = Gallery
#                 fields = []

#             def save(self, commit=True):
#                 instance = super().save(commit)
#                 for img in self.cleaned_data['images']:
#                     GalleryImage.objects.create(gallery=instance, image=img)
#                 return instance

#         return GalleryForm
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    readonly_fields = ("preview",)
    fields = ("image", "preview")

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:70px;border-radius:5px;" />',
                obj.image.url
            )
        return ""


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm
    inlines = [GalleryImageInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    search_fields = ('full_name', 'email', 'subject')
    list_filter = ('created_at',)
    