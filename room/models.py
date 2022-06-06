from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.urls import reverse
from django.db.models import Avg, Count
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class Category(MPTTModel):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    parent = TreeForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='children',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



class MPTTMeta:
    order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path[::-1])


class Rooms(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    price_one = models.CharField(max_length=255,blank=True)
    price_two = models.CharField(max_length=255,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'self': self.slug})


class Images(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(blank=True, upload_to='images/')
    # def __str__(self):
    #     return self.room



class Comment(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=55, blank=True)
    comment = models.TextField(max_length=255,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','phone', 'comment', 'rate']



    def avaregereview(self):
        reviews = Comment.objects.filter(room=self, status='True').aggregate(avarage=Avg('rate'))
        avg = 0
        if reviews["avarage"] is not None:
            avg = float(reviews["avarage"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(room=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class Order(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('accepted', 'qabul qilingan'),
    )

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    pay = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    guest = models.IntegerField()
    arrival = models.CharField(max_length=50)
    departure = models.CharField(max_length=20)
    room = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    select = models.CharField(max_length=100)
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Business(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    descriptions = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Restourant(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    descriptions = models.TextField(blank=True)
    def __str__(self):
        return self.title


class Spa(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    descriptions = models.TextField(blank=True)
    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title



class Services(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    descriptions = models.TextField(blank=True)
    def __str__(self):
        return self.title





class Aboutus(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    descriptions = models.TextField(blank=True)
    def __str__(self):
        return self.title

