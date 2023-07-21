from modeltranslation.translator import translator, TranslationOptions
from .models import BlogPost

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    required_fields = ('de', 'en')

translator.register(BlogPost, BlogPostTranslationOptions)