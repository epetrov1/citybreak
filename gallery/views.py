from django.shortcuts import render
from .models import Gallery
from django.urls import reverse
from django.views.generic import ListView
from django.http import Http404


class GalleryView(ListView):
    model = Gallery
    order_by = ['-day_publish']

def slide_show_view(request, *args, **kwargs):
    try:
        all_images = Gallery.objects.all()
        chosen_image = Gallery.objects.get(**kwargs)
        image_id = chosen_image.id

        context = {
            'all_images': all_images,
            'chosen_image': chosen_image,
            'image_id': image_id
        }
    except Gallery.DoesNotExist:
        raise Http404("This image does not exist.")
    return render(request, "gallery/gallery_slide.html", context)