from modeltranslation.translator import register, TranslationOptions
from home.models import FAQ, Informations, Special_offers, Bussiness_detail, Restourant_detail


@register(Informations)
class InformationsTranslationOptions(TranslationOptions):
    fields = ('title','address','description',)

@register(FAQ)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(Special_offers)
class Special_offersTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Bussiness_detail)
class Bussiness_detailTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Restourant_detail)
class Bussiness_detailTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)