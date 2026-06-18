from django.shortcuts import render, get_object_or_404, redirect
from .models import Sermon, Event, Gallery, GalleryImage, ContactMessage
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'index.html')


def sermon(request):
    sermons = Sermon.objects.all()

    context = {
        'sermons': sermons
    }

    return render(request, 'sermon.html', context)


def event(request):
    events = Event.objects.order_by('event_date')
    featured_event = Event.objects.filter(featured=True).first()

    return render(request, 'event.html', {
        'events': events,
        'featured_event': featured_event,
    })

def gallery(request):
    gallery_images = GalleryImage.objects.all().order_by('-id')

    return render(request, 'gallery.html', {
        'gallery_images': gallery_images
    })

def about(request):
    return render(request, 'about.html')    

def contact(request):
    return render(request, 'contact.html')


@csrf_exempt
def upload_gallery_images(request, gallery_id):
    if request.method == "POST":

        gallery = get_object_or_404(Gallery, id=gallery_id)

        files = request.FILES.getlist("file")

        for f in files:
            GalleryImage.objects.create(
                gallery=gallery,
                image=f
            )

        return JsonResponse({"message": "uploaded successfully"})

    return JsonResponse({"error": "invalid request"}, status=400)


def upload_gallery_page(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)

    return render(request, "gallery_upload.html", {
        "gallery": gallery
    })

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')

    return render(request, 'contact.html')