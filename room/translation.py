from modeltranslation.translator import register, TranslationOptions
from room.models import Category, Rooms, Services, Aboutus, Business, Restourant, Spa, Slider


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Rooms)
class RoomsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'price_one', 'price_two',)


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Aboutus)
class AboutusTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Business)
class BusinessTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Restourant)
class RestourantTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Spa)
class RestourantTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('title',)