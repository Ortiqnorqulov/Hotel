from django.shortcuts import render, redirect
from home.forms import OrderForm, ContactForm
from home.models import Informations, ContactMessage, FAQ, Special_offers, Bussiness_detail, Restourant_detail, Gallery

from room.models import Category, Rooms, Images, Comment, Order, \
    Aboutus, Business, Restourant, Spa, Slider, Services
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.contrib import messages
from django.utils import translation
from django.http import HttpResponseRedirect




from home.serializers import IndexPageSerializer, InformationsSerializer, CategoryDetailSerializer, \
    RoomDetailSerializer, ContactUsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from home.pagination import CustomPagination
from rest_framework.generics import ListAPIView
from rest_framework import status


class InfoPage(APIView):
    def get(self, request):
        info = Informations.objects.all()
        serializer = InformationsSerializer(info, many=True)
        return Response(serializer.data)

########################################################################################################################
########################################################################################################################
########################################################################################################################


class IndexPage(APIView):
    def get(self, request):
        room_slider = Rooms.objects.filter(status='True').order_by('id')[:5]
        serializer = IndexPageSerializer(room_slider, many=True)
        return Response(serializer.data)


def home(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    room_slider = Rooms.objects.all().order_by('id')[:5]
    room_latest = Rooms.objects.all().order_by('id')
    room_picked = Rooms.objects.all().order_by('?')[:5]
    business = Business.objects.all().order_by('id')
    restourant = Restourant.objects.all().order_by('id')
    spa = Spa.objects.all().order_by('id')
    slider = Slider.objects.all().order_by('id')
    spesial = Special_offers.objects.all().order_by('id')
    comments = Comment.objects.all()
    context = {
        'info': info,
        'category': category,
        'room_slider': room_slider,
        'room_latest': room_latest,
        'room_picked': room_picked,
        'comments':comments,
        'bussines':business,
        'restourant':restourant,
        'spa':spa,
        'slider':slider,
        'spesial':spesial,
    }
    return render(request, 'index.html', context)
########################################################################################################################
########################################################################################################################
########################################################################################################################

def special_offers(request,id):
    info = Informations.objects.all()
    special = Special_offers.objects.get(pk=id)
    context = {
        'special':special,
        'info':info,
    }
    return render(request, 'special.html', context)

########################################################################################################################
###################################### ROOM DETAILS ####################################################################
########################################################################################################################


class RoomDetailPage(APIView):
    def get(self, request, id, slug):
        roomdetail = Rooms.objects.get(pk=id)
        serializer = RoomDetailSerializer(roomdetail)
        return Response(serializer.data)


def room_detail(request, id, slug):
    category = Category.objects.all()
    info = Informations.objects.all()
    room_slider = Rooms.objects.all().order_by('id')[:5]
    room_latest = Rooms.objects.all().order_by('-id')[:5]
    room_picked = Rooms.objects.all().order_by('?')[:3]
    rooms_page = Rooms.objects.get(pk=id)
    images = Images.objects.filter(room_id=id)
    comments = Comment.objects.filter(room_id=id, status='True')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.citizenship = form.cleaned_data['citizenship']
            data.pay = form.cleaned_data['pay']
            data.email = form.cleaned_data['email']
            data.guest = form.cleaned_data['guest']
            data.arrival = form.cleaned_data['arrival']
            data.departure = form.cleaned_data['departure']
            data.room = form.cleaned_data['room']
            data.category = form.cleaned_data['category']
            data.select = form.cleaned_data['select']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Siz xonani bro'n qildiz aperato'r siz bilan bog'lanadi")
            return redirect('home')
    form = OrderForm
    context = {
        'category': category,
        'info': info,
        'rooms_page': rooms_page,
        'images': images,
        'comments': comments,
        'room_slider': room_slider,
        'room_latest': room_latest,
        'room_picked': room_picked,
        'form':form,
    }
    return render(request, 'room_detail.html', context)

########################################################################################################################
#################################### CATEGORY DETAILS ##################################################################
########################################################################################################################

class RoomsPage(APIView):
    def get(self, request, id):
        room_slider = Rooms.objects.filter(category_id=id)
        serializer = CategoryDetailSerializer(room_slider, many=True)
        return Response(serializer.data)

def category_room(request,id, slug):
    category = Category.objects.all()
    info = Informations.objects.all()
    room_slider = Rooms.objects.all().order_by('id')[:5]
    room_latest = Rooms.objects.all().order_by('-id')[:5]
    room_picked = Rooms.objects.all().order_by('?')[:3]
    rooms_page = Rooms.objects.filter(category_id=id)
    paginator = Paginator(rooms_page, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        rooms_page = paginator.page(page)
    except PageNotAnInteger:
        rooms_page = paginator.page(1)
    except EmptyPage:
        rooms_page = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'rooms_page': rooms_page,
        'info' : info,
        'room_slider': room_slider,
        'room_latest': room_latest,
        'room_picked': room_picked,
    }
    return render(request, 'category_room.html', context)
########################################################################################################################
########################################################################################################################
########################################################################################################################





###########################################################################
def aboutus(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    aboutus = Aboutus.objects.all().order_by('id')
    context = {
        'info': info,
        'category': category,
        'aboutus': aboutus,

    }
    return render(request, 'aboutus.html', context)



def aboutus_detail(request,id):
    info = Informations.objects.all()
    category = Category.objects.all()
    about = Aboutus.objects.get(pk=id)
    context = {
        'info': info,
        'category': category,
        'about': about,

    }
    return render(request, 'aboutus_detail.html', context)

################################################################################
class ContactUs(APIView):
    def post(self, request):
        serilaizer = ContactUsSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        messages.error(request, "Kechirasiz texnik ishlar sababli xabaringiz bormadi")
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


def contactus(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.phone = form.cleaned_data['phone']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return redirect('home')
    info = Informations.objects.all()
    room = Rooms.objects.all().order_by('?')[:3]
    category = Category.objects.all()
    form = ContactForm
    context = {'info': info,
               'form': form,
               'room':room,
               'category':category,}
    return render(request,'contact.html', context)



def faq(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    faq = FAQ.objects.filter(status='True').order_by('ordernumber')
    context = {'category': category,
                'faq': faq,
                'info': info
                }
    return render(request, 'faq.html', context)


def bussines_detail(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    bussiness_detail = Bussiness_detail.objects.all()
    context = {
        'info': info,
        'category': category,
        'bussiness_detail': bussiness_detail,
     }
    return render(request, 'bussiness_detail.html', context)


def restourant_detail(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    restourant_detail = Restourant_detail.objects.all()
    context = {
        'info': info,
        'category': category,
        'restourant_detail': restourant_detail,
     }
    return render(request, 'restourant_detail.html', context)

def gallery(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    gellery = Gallery.objects.all()
    context = {
        'info': info,
        'category': category,
        'gellery': gellery,
     }
    return render(request, 'gallery.html', context)



def services(request):
    info = Informations.objects.all()
    category = Category.objects.all()
    services_slider = Services.objects.all()
    context = {
        'info': info,
        'category': category,
        'services_slider': services_slider,
     }
    return render(request, 'services.html', context)



def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        return HttpResponseRedirect("/"+lang)