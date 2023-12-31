from django.db import models
from datetime import datetime
from slugify import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_create = models.DateField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        return reverse('detail_blog', kwargs={'slug': self.slug})
        
    def __str__(self):
        return self.title