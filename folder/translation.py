from modeltranslation.translator import register, TranslationOptions
from .models import Folder

@register(Folder)
class FolderModelTranslationOptions(TranslationOptions):
    fields = ("title", "description")
