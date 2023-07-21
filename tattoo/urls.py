from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls')),
    path('ticket/', include('ticket.urls')),
    path('blog/', include('blog.urls')),
    path('', include('pages.urls')),
    path('faq/', include('faq.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += i18n_patterns (
    path('gallery/', include("gallery.urls")), 
    path('ticket/', include('ticket.urls')),  
    path('blog/', include("blog.urls")),
    path('', include("pages.urls")),
    path('faq/', include('faq.urls')),
    path('summernote/', include('django_summernote.urls')),
) 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]