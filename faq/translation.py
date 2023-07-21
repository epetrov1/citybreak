from modeltranslation.translator import translator, TranslationOptions
from .models import Faq

class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)

translator.register(Faq, FaqTranslationOptions)