from django.contrib import admin
from django.urls import path
from MIGCWEBS import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sermon/', views.sermon, name='sermon'),
    path('event/', views.event, name='event'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("gallery/upload/<int:gallery_id>/", views.upload_gallery_page, name="gallery_upload_page"),
    path("gallery/upload/api/<int:gallery_id>/", views.upload_gallery_images, name="gallery_upload_api"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)