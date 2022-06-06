from rest_framework import serializers

from home.models import Informations, ContactMessage
from room.models import Rooms, Category, Images


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('parent', 'title', 'description', 'image', 'status', 'slug')



class IndexPageSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Rooms
        fields = "__all__"


class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informations
        fields = "__all__"



class CategoryDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Rooms
        fields = ('id','category', 'title_uz','title_en','title_ru', 'price_one_uz','price_one_en','price_one_ru', 'price_two_uz','price_two_en','price_two_ru', 'image', 'description_uz','description_en','description_ru',)



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class RoomDetailSerializer(serializers.ModelSerializer):
   category = serializers.SlugRelatedField(slug_field='title', read_only=True)
   images = ImageSerializer(many=True,read_only=True)
   class Meta:
        model = Rooms
        fields = ('id', 'category', 'title_uz','title_en','title_ru', 'price_one_uz','price_one_en','price_one_ru', 'price_two_uz','price_two_en','price_two_ru', 'image', 'description_uz','description_en','description_ru', 'images','create_at','update_at',)


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'subject', 'message',)