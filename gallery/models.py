from django.db import models
from django.urls import reverse
from PIL import Image

class Gallery(models.Model):
    name = models.CharField(max_length=250)
    new_image = models.ImageField(upload_to='gallery_folder')
    day_publish = models.DateField()

    def save(self, *args, **kwargs):
        super().save(self, *args, **kwargs)
        img = Image.open(self.new_image.path)
        if img.height > 940 or img.width > 788:
            output_size = (820,720)
            img.thumbnail(output_size)
            img.save(self.new_image.path)

    def get_absolute_url(self):
        return reverse('detail-slug', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name