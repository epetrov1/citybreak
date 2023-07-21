from django.contrib import admin
from . models import Faq
from django_summernote.admin import SummernoteModelAdmin



class FaqPostAdmin(SummernoteModelAdmin):  
    list_display = ('id',)
    summernote_fields = ('answer', 'answer_bg', 'answer_en')

admin.site.register(Faq, FaqPostAdmin)
