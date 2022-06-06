from django.contrib import admin
from room.models import Category, Rooms, Images, Comment, Order,  Services, \
    Aboutus, Business, Restourant, Spa, Slider
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TranslationAdmin



class CategoryAdmin(TranslationAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title']



class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title','related_rooms_page_count', 'related_rooms_page_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs,
            Rooms,
            'category',
            'rooms_page_cumulative_count',
            cumulative=True
        )

        qs = Category.objects.add_related_count(
            qs,
            Rooms,
            'category',
            'rooms_page_count',
            cumulative=False
        )
        return qs
    def related_rooms_page_count(self, instance):
        return instance.rooms_page_count
    related_rooms_page_count.short_description = 'Related rooms_page (for this specific category)'
    def related_rooms_page_cumulative_count(self,instance):
        return instance.rooms_page_cumulative_count
    related_rooms_page_cumulative_count.short_description = 'Related rooms_page (in tree)'


class RoomsImageInline(admin.TabularInline):
    model = Images
    extra = 5

class RoomsAdmin(TranslationAdmin):
    list_display = ['category', 'title', 'price_one', 'price_two', 'status', 'image_tag',]
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [RoomsImageInline]
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'comment', 'status',]
    list_filter = ['status']
    readonly_fields = ('name', 'phone', 'comment', 'ip',  'room', 'rate')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'citizenship', 'pay','email', 'guest', 'arrival', 'departure', 'room', 'category',  'ip',]
    list_filter = ['status']


class BusinessAdmin(TranslationAdmin):
    list_display = ['title',  'image', 'descriptions',]



class RestourantAdmin(TranslationAdmin):
    list_display = ['title', 'image',  'descriptions',]

class SpaAdmin(TranslationAdmin):
    list_display = ['title',  'image', 'descriptions',]

class SliderAdmin(TranslationAdmin):
    list_display = ['title',  'image',]



class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'descriptions',]



class AboutusAdmin(TranslationAdmin):
    list_display = ['title',  'image', 'descriptions',]


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Images)
admin.site.register(Order, OrderAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Restourant, RestourantAdmin)
admin.site.register(Spa, SpaAdmin)
admin.site.register(Slider, SliderAdmin)