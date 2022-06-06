from django.db import models
from django.forms import TextInput, EmailInput, Textarea, ModelForm


class Informations(models.Model):
    STATUS =(
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(blank=True, max_length=20)
    email = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True,upload_to='images/')
    telegram = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




class ContactMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', 'Read'),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=255)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True, max_length=100)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name






class FAQ(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False','Yopilgan'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=1000)
    answer = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question



class Special_offers(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Bussiness_detail(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Restourant_detail(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title