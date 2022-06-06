from django.contrib import admin
from home.models import Informations, ContactMessage, FAQ, Special_offers, Bussiness_detail, Restourant_detail, Gallery
from modeltranslation.admin import TranslationAdmin

class InformationsAdmin(TranslationAdmin):
    list_display = ['title', 'country', 'city', 'address', 'phone', 'status', 'create_at',]



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'phone', 'email', 'message', 'creat_at',]
    readonly_fields = ('name', 'subject', 'phone', 'email', 'message', 'ip','creat_at',)
    list_filter = ['status']


class FAQAdmin(TranslationAdmin):
    list_display = ['question', 'answer', 'ordernumber', 'status']
    list_filter = ['status']

class Special_offersAdmin(TranslationAdmin):
    list_display = ['title', 'image', 'description',]

class Bussiness_detailAdmin(TranslationAdmin):
    list_display = ['title', 'image', 'description',]

class Restourant_detailAdmin(TranslationAdmin):
    list_display = ['title', 'image', 'description',]

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','image']


admin.site.register(Informations, InformationsAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Special_offers, Special_offersAdmin)
admin.site.register(Bussiness_detail, Bussiness_detailAdmin)
admin.site.register(Restourant_detail, Restourant_detailAdmin)
admin.site.register(Gallery, GalleryAdmin)