from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils import translation
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from blog.models import Blog
from creatoradmin.forms import RegisterForm, AddCategoryForm, AddRoomForm, FaqForm, UserUpdateForm, CreatorUpdateForm, \
    StaffUpdateForm, AdminNoteForm, CategoryEdit, EditRoom, FaqEditForm, AddInfo, EditInfo, AddBlog, EditBlog, \
    CreateServices, EditServices, \
    CreateAbout, EditAbout, AddBussines, EditBussines, AddRestourant, EditRestourant, AddSpa, EditSpa, AddSpecial, \
    EditSpecial, CreateResDetail, EditResDetail, CreateBussinesDetail, EditBussinesDetail, EditContact, RegNoteForm, \
    EditContactReg, CreateSlider, EditSlider, RoomSlider, EditRoomSlider
from creatoradmin.models import CustomUser, Registration, Creator
from home.models import FAQ, Informations, ContactMessage, Special_offers, Restourant_detail, Bussiness_detail
from room.models import Category, Rooms, Order, Comment, Services, Aboutus, Business, Restourant, Spa, Slider, Images


#################################################################################################################
#################################################################################################################
#################################### USERLARGA TEGISHLI BO'LIM ##################################################

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            user.save()
            login(request, user)
            current_user = CustomUser.objects.get(email=request.user.email)
            if current_user.user_type == CustomUser.Registration:
                Registration.objects.create(user=user)
                messages.success(request, 'Your account has been created')
                return redirect('home')
        else:
            messages.warning(request, "Registration error!")
            return HttpResponseRedirect('/')
    form = RegisterForm()
    return render(request, 'profile/signup_form.html', {'form': form})


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Error Try Again Later')
            return redirect('login_form')
    return render(request, 'profile/login.html')


def logout_form(request):
    logout(request)
    return redirect('home')




def user_update(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You profile successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Eror password')
            return redirect(url)
    else:
        form = UserUpdateForm(instance=request.user)
        return render(request, 'profile/user_update.html', {'form': form})




@login_required(login_url='login_form')
def user_password(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your profile password successfully updated')
            return redirect('home')
        else:
            messages.error(request, 'Eror password')
            return redirect(url)
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'profile/user_password.html', {'form': form})



class CreatorUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        creatoradmin = Creator.objects.get(user=self.request.user)
        form = CreatorUpdateForm(instance=creatoradmin)
        context = {'form': form}
        return render(request, 'profile/profile_update.html', context)

    def post(self, *args, **kwargs):
        form = CreatorUpdateForm(self.request.POST, self.request.FILES, instance=self.request.user.creator)
        if form.is_valid():
            form.save()
            return redirect(reverse('creatoradmin'))
        return redirect('home')

class RegistrationUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        registration = Registration.objects.get(user=self.request.user)
        form = StaffUpdateForm(instance=registration)
        context = {'form': form}
        return render(request, 'profile/registration_update.html', context)

    def post(self, *args, **kwargs):
        form = StaffUpdateForm(self.request.POST, self.request.FILES, instance=self.request.user.registration)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration'))
        return redirect('home')



#################################################################################################################
#################################################################################################################
###################################### USER TYPE PAGE ###########################################################

@login_required(login_url='login_form')
def registration(request):
    try:
        user = Registration.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')
    room = Rooms.objects.all()
    room_count = room.count()
    category = Category.objects.all()
    category_count = category.count()
    order = Order.objects.all()
    order_count = order.count()
    comment = Comment.objects.all()
    comment_count = comment.count()
    contact = ContactMessage.objects.all()
    contact_count = contact.count()
    users = Registration.objects.all().order_by('id')
    blog = Blog.objects.all()
    blog_count = blog.count()
    context = {
        'user': user,
        'room': room,
        'room_count': room_count,
        'category': category,
        'category_count': category_count,
        'order': order,
        'order_count': order_count,
        'comment': comment,
        'comment_count': comment_count,
        'contact': contact,
        'contact_count': contact_count,
        'users': users,
        'blog': blog,
        'blog_count': blog_count,
    }
    return render(request, 'registration/registration.html', context)



@login_required(login_url='login_form')
def creatoradmin(request):
    try:
        admin = Creator.objects.get(user=request.user)
    except:
        messages.warning(request, 'Error Try Again Later')
        return redirect('login_form')
    room = Rooms.objects.all()
    room_count = room.count()
    category = Category.objects.all()
    category_count = category.count()
    order = Order.objects.all()
    order_count = order.count()
    comment = Comment.objects.all()
    comment_count = comment.count()
    contact = ContactMessage.objects.all()
    contact_count = contact.count()
    users = Registration.objects.all().order_by('id')
    blog = Blog.objects.all()
    blog_count = blog.count()
    context = {
        'admin': admin,
        'room':room,
        'room_count': room_count,
        'category':category,
        'category_count':category_count,
        'order':order,
        'order_count':order_count,
        'comment':comment,
        'comment_count':comment_count,
        'contact':contact,
        'contact_count':contact_count,
        'users':users,
        'blog':blog,
        'blog_count':blog_count,
    }
    return render(request, 'admin/admin.html', context)




#################################################################################################################
#################################################################################################################
###################################### CATEGO'RYALAR BO'LIMI ####################################################


def createcategory(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = Category()
            category.title_uz = form.cleaned_data.get('title_uz')
            category.title_en = form.cleaned_data.get('title_en')
            category.title_ru = form.cleaned_data.get('title_ru')
            category.description_uz = form.cleaned_data.get('description_uz')
            category.description_en = form.cleaned_data.get('description_en')
            category.description_ru = form.cleaned_data.get('description_ru')
            if request.FILES:
                category.image = request.FILES['image']
            category.slug = form.cleaned_data.get('slug')
            category.status = form.cleaned_data.get('status')
            category.save()
            return redirect('category_update')
    form = AddCategoryForm()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'category/add_category.html', context)



def category_update(request):
    category = Category.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'category': category,
        'admin': admin,
    }

    return render(request, 'category/category_update.html', context)





def category_edit(request, id, slug):
    category = Category.objects.get(pk=id)
    admin = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = CategoryEdit(request.POST, request.FILES, instance=category)
        if request.FILES:
            category.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('category_update')
    else:
        form = CategoryEdit(instance=category)
        context = {'form': form,
                   'admin': admin}

        return render(request, 'category/category_edit.html', context)




def category_delate(request, id, slug):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('category_update')

#################################################################################################################
#################################################################################################################
######################################### HONALAR BO'LIMI #######################################################

def createroom(request):
    if request.method == 'POST':
        form = AddRoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = Rooms()
            room.title_uz = form.cleaned_data.get('title_uz')
            room.title_en = form.cleaned_data.get('title_en')
            room.title_ru = form.cleaned_data.get('title_ru')
            room.price_one_uz = form.cleaned_data.get('price_one_uz')
            room.price_one_en = form.cleaned_data.get('price_one_en')
            room.price_one_ru = form.cleaned_data.get('price_one_ru')
            room.price_two_uz = form.cleaned_data.get('price_two_uz')
            room.price_two_en = form.cleaned_data.get('price_two_en')
            room.price_two_ru = form.cleaned_data.get('price_two_ru')
            room.description_uz = form.cleaned_data.get('description_uz')
            room.description_en = form.cleaned_data.get('description_en')
            room.description_ru = form.cleaned_data.get('description_ru')
            room.category = form.cleaned_data.get('category')
            if request.FILES:
                room.image = request.FILES['image']
            room.slug = form.cleaned_data.get('slug')
            room.status = form.cleaned_data.get('status')
            room.save()
            return redirect('room_update')
    form = AddRoomForm()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'room/add_room.html', context)




def room_update(request):
    room = Rooms.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'room': room,
        'admin': admin,
    }

    return render(request, 'room/room_update.html', context)


def room_edit(request, id, slug):
    admin = Creator.objects.get(user=request.user)
    room = Rooms.objects.get(pk=id)
    if request.method == 'POST':
        form = EditRoom(request.POST, request.FILES, instance=room)
        if request.FILES:
            room.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('room_update')
    else:
        form = EditRoom(instance=room)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'room/room_edit.html', context)

def room_delate(request, id, slug):
    room = Rooms.objects.get(pk=id)
    room.delete()
    return redirect('room_update')

#################################################################################################################
#################################################################################################################
########################################### FAQ BO'LIMI #########################################################


def faqs(request):
    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            faq = FAQ()
            faq.ordernumber = form.cleaned_data.get('ordernumber')
            faq.question_uz = form.cleaned_data.get('question_uz')
            faq.question_en = form.cleaned_data.get('question_en')
            faq.question_ru = form.cleaned_data.get('question_ru')
            faq.answer_uz = form.cleaned_data.get('answer_uz')
            faq.answer_en = form.cleaned_data.get('answer_en')
            faq.answer_ru = form.cleaned_data.get('answer_ru')
            faq.status = form.cleaned_data.get('status')
            faq.save()
            return redirect('creatoradmin')
    form = FaqForm()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'faq/faqs.html', context)



def faq_update(request):
    faq = FAQ.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'faq': faq,
        'admin': admin,
    }

    return render(request, 'faq/faq_update.html', context)



def faq_edit(request, id):
    admin = Creator.objects.get(user=request.user)
    faqss = FAQ.objects.get(pk=id)
    if request.method == 'POST':
        form = FaqEditForm(request.POST, instance=faqss)
        if form.is_valid():
            form.save()
            return redirect('faq_update')
    else:
        form = FaqEditForm(instance=faqss)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'faq/faq_edit.html', context)


def faq_delate(request, id,):
    faqsss = FAQ.objects.get(pk=id)
    faqsss.delete()
    return redirect('faq_update')


#################################################################################################################
#################################################################################################################
##################################### ORDERLAR BO'LIMI ##########################################################



def orderdetail(request):
    info = Informations.objects.all().order_by('id')
    roomlist = Rooms.objects.all().order_by('id')
    roomcategory = Category.objects.all().order_by('id')
    orderdetail = Order.objects.all().order_by('id')
    paginator = Paginator(orderdetail, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        orderdetail = paginator.page(page)
    except PageNotAnInteger:
        orderdetail = paginator.page(1)
    except EmptyPage:
        orderdetail = paginator.page(paginator.num_pages)
    admin = Creator.objects.get(user=request.user)
    context = {
        'info': info,
        'roomlist': roomlist,
        'roomcategory': roomcategory,
        'orderdetail': orderdetail,
        'admin': admin,
        'page':page,
    }
    return render(request, 'order/orderlist.html', context)


def admin_note(request, id):
    order = Order.objects.get(pk=id)
    admin = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = AdminNoteForm(request.POST,  instance=order)
        if form.is_valid():
            form.save()
            return redirect('orderdetail')
    else:
        form = AdminNoteForm(instance=order)
        context = {'form': form,
                'admin': admin,
                'order':order,
                  }

        return render(request, 'order/admin_note.html', context)



def order_delate(request, id):
    orders = Order.objects.get(pk=id)
    orders.delete()
    return redirect('orderdetail')

#################################################################################################################
#################################################################################################################
######################################### COMMENTLAR BO'LIMI ####################################################
def comment(request):
    room = Rooms.objects.all().order_by('id')
    comment = Comment.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'room':room,
        'comment':comment,
        'admin':admin,
    }
    return render(request, 'comment/comment.html', context)


def comment_delate(request, id,):
    comments = Comment.objects.get(pk=id)
    comments.delete()
    return redirect('comment')


#################################################################################################################
#################################################################################################################
################################## CONTACT BOLIMI ###############################################################
def contact_messages(request):
    contact = ContactMessage.objects.all().order_by('id')
    paginator = Paginator(contact, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    admin = Creator.objects.get(user=request.user)
    context = {
        'contact': contact,
        'admin': admin,
        'page':page,
    }

    return render(request, 'contact/contact_admin.html', context)


def status_contact(request, id):
    contact = ContactMessage.objects.get(pk=id)
    admin = Creator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditContact(request.POST,  instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_messages')
    else:
        form = EditContact(instance=contact)
        context = {'form': form,
                'admin': admin,
                'order':contact,
                  }

        return render(request, 'contact/contact_status.html', context)

def contact_delate(request, id,):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_messages')
#################################################################################################################
#################################################################################################################
######################################### INFORMATIONS BO'LIMI ##################################################
def createinfo(request):
    if request.method == 'POST':
        form = AddInfo(request.POST, request.FILES)
        if form.is_valid():
            info = Informations()
            info.title_uz = form.cleaned_data.get('title_uz')
            info.title_en = form.cleaned_data.get('title_en')
            info.title_ru = form.cleaned_data.get('title_ru')
            info.country = form.cleaned_data.get('country')
            info.city = form.cleaned_data.get('city')
            info.address_uz = form.cleaned_data.get('address_uz')
            info.address_en = form.cleaned_data.get('address_en')
            info.address_ru = form.cleaned_data.get('address_ru')
            info.phone = form.cleaned_data.get('phone')
            info.email = form.cleaned_data.get('email')
            if request.FILES:
                info.image = request.FILES['image']
            info.telegram = form.cleaned_data.get('telegram')
            info.instagram = form.cleaned_data.get('instagram')
            info.description_uz = form.cleaned_data.get('description_uz')
            info.description_en = form.cleaned_data.get('description_en')
            info.description_ru = form.cleaned_data.get('description_ru')
            info.status = form.cleaned_data.get('status')
            info.save()
            return redirect('creatoradmin')
    form = AddInfo()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'information/addinfo.html', context)



def info_update(request):
    info = Informations.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'info': info,
        'admin': admin,
    }

    return render(request, 'information/info_update.html', context)



def info_edit(request, id):
    admin = Creator.objects.get(user=request.user)
    info = Informations.objects.get(pk=id)
    if request.method == 'POST':
        form = EditInfo(request.POST, request.FILES, instance=info)
        if request.FILES:
            info.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('info_update')
    else:
        form = EditInfo(instance=info)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'information/info_edit.html', context)



def info_delate(request, id):
    info = Informations.objects.get(pk=id)
    info.delete()
    return redirect('info_update')

#################################################################################################################
#################################################################################################################
############################################ BLOG BO'LIMI #######################################################
def createblog(request):
    if request.method == 'POST':
        form = AddBlog(request.POST, request.FILES)
        if form.is_valid():
            blog = Blog()
            blog.title_uz = form.cleaned_data.get('title_uz')
            blog.title_en = form.cleaned_data.get('title_en')
            blog.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                blog.image = request.FILES['image']
            blog.description_uz = form.cleaned_data.get('description_uz')
            blog.description_en = form.cleaned_data.get('description_en')
            blog.description_ru = form.cleaned_data.get('description_ru')
            blog.status = form.cleaned_data.get('status')
            blog.save()
            return redirect('blog_update')
    form = AddBlog()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'blog/createblog.html', context)



def blog_update(request):
    blog = Blog.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    paginator = Paginator(blog, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    context = {
        'blog': blog,
        'admin': admin,
        'page':page,
    }

    return render(request, 'blog/blog_update.html', context)




def blog_edit(request, id):
    admin = Creator.objects.get(user=request.user)
    blog = Blog.objects.get(pk=id)
    if request.method == 'POST':
        form = EditBlog(request.POST, request.FILES, instance=blog)
        if request.FILES:
            blog.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('blog_update')
    else:
        form = EditBlog(instance=blog)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'blog/blog_edit.html', context)



def blog_delate(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('blog_update')

#################################################################################################################
#################################################################################################################
#################################### BUSSINES BO'LIMI ##########################################################
def createbussines(request):
    if request.method == 'POST':
        form = AddBussines(request.POST, request.FILES)
        if form.is_valid():
            bussines = Business()
            bussines.title_uz = form.cleaned_data.get('title_uz')
            bussines.title_en = form.cleaned_data.get('title_en')
            bussines.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                bussines.image = request.FILES['image']
            bussines.descriptions_uz = form.cleaned_data.get('descriptions_uz')
            bussines.descriptions_en = form.cleaned_data.get('descriptions_en')
            bussines.descriptions_ru = form.cleaned_data.get('descriptions_ru')
            bussines.save()
            return redirect('update_businnes')
    form = AddBussines()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'bussines/addbussines.html', context)



def update_businnes(request):
    bussines = Business.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'bussines': bussines,
        'admin': admin,
    }

    return render(request, 'bussines/update_bussines.html', context)


def edit_bussines(request, id):
    admin = Creator.objects.get(user=request.user)
    bussines = Business.objects.get(pk=id)
    if request.method == 'POST':
        form = EditBussines(request.POST, request.FILES, instance=bussines)
        if request.FILES:
            bussines.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_businnes')
    else:
        form = EditBussines(instance=bussines)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'bussines/edit_bussines.html', context)


def bussines_delete(request, id):
    bussines = Business.objects.get(pk=id)
    bussines.delete()
    return redirect('update_businnes')

#################################################################################################################
#################################################################################################################
#################################### RESTOURANT BO'LIMI ##############################################################
def create_restourant(request):
    if request.method == 'POST':
        form = AddRestourant(request.POST, request.FILES)
        if form.is_valid():
            restourant = Restourant()
            restourant.title_uz = form.cleaned_data.get('title_uz')
            restourant.title_en = form.cleaned_data.get('title_en')
            restourant.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                restourant.image = request.FILES['image']
            restourant.descriptions_uz = form.cleaned_data.get('descriptions_uz')
            restourant.descriptions_en = form.cleaned_data.get('descriptions_en')
            restourant.descriptions_ru = form.cleaned_data.get('descriptions_ru')
            restourant.save()
            return redirect('update_restourant')
    form = AddRestourant()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'restourant/restourant.html', context)


def update_restourant(request):
    restourant = Restourant.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'restourant': restourant,
        'admin': admin,
    }

    return render(request, 'restourant/update_restourant.html', context)



def edit_restourant(request, id):
    admin = Creator.objects.get(user=request.user)
    restourant = Restourant.objects.get(pk=id)
    if request.method == 'POST':
        form = EditRestourant(request.POST, request.FILES, instance=restourant)
        if request.FILES:
            restourant.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_restourant')
    else:
        form = EditRestourant(instance=restourant)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'restourant/edit_restourant.html', context)


def restourant_delete(request, id):
    restourant = Restourant.objects.get(pk=id)
    restourant.delete()
    return redirect('update_restourant')
#################################################################################################################
#################################################################################################################
#################################### SPA BO'LIMI #############################################################
def create_spa(request):
    if request.method == 'POST':
        form = AddSpa(request.POST, request.FILES)
        if form.is_valid():
            spa = Spa()
            spa.title_uz = form.cleaned_data.get('title_uz')
            spa.title_en = form.cleaned_data.get('title_en')
            spa.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                spa.image = request.FILES['image']
            spa.descriptions_uz = form.cleaned_data.get('descriptions_uz')
            spa.descriptions_en = form.cleaned_data.get('descriptions_en')
            spa.descriptions_ru = form.cleaned_data.get('descriptions_ru')
            spa.save()
            return redirect('update_spa')
    form = AddSpa()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'spa/addspa.html', context)


def update_spa(request):
    spa = Spa.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'spa': spa,
        'admin': admin,
    }

    return render(request, 'spa/update_spa.html', context)


def edit_spa(request, id):
    admin = Creator.objects.get(user=request.user)
    spa = Spa.objects.get(pk=id)
    if request.method == 'POST':
        form = EditSpa(request.POST, request.FILES, instance=spa)
        if request.FILES:
            spa.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_spa')
    else:
        form = EditSpa(instance=spa)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'spa/edit_spa.html', context)


def spa_delete(request, id):
    spa = Spa.objects.get(pk=id)
    spa.delete()
    return redirect('update_spa')
#################################################################################################################
#################################################################################################################
#################################### SPESIAL OFFERS BO'LIMI #####################################################
def create_special(request):
    if request.method == 'POST':
        form = AddSpecial(request.POST, request.FILES)
        if form.is_valid():
            special = Special_offers()
            special.title_uz = form.cleaned_data.get('title_uz')
            special.title_en = form.cleaned_data.get('title_en')
            special.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                special.image = request.FILES['image']
            special.description_uz = form.cleaned_data.get('description_uz')
            special.description_en = form.cleaned_data.get('description_en')
            special.description_ru = form.cleaned_data.get('description_ru')
            special.save()
            return redirect('update_special')
    form = AddSpecial()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'special/addspecial.html', context)


def update_special(request):
    special = Special_offers.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'special': special,
        'admin': admin,
    }

    return render(request, 'special/update_special.html', context)


def edit_special(request, id):
    admin = Creator.objects.get(user=request.user)
    special = Special_offers.objects.get(pk=id)
    if request.method == 'POST':
        form = EditSpecial(request.POST, request.FILES, instance=special)
        if request.FILES:
            special.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_special')
    else:
        form = EditSpecial(instance=special)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'special/edit_special.html', context)


def special_delete(request, id):
    special = Special_offers.objects.get(pk=id)
    special.delete()
    return redirect('update_special')
#################################################################################################################
#################################################################################################################
#################################### RESTOURANT DETAIL BO'LIMI ##################################################
def create_resdetail(request):
    if request.method == 'POST':
        form = CreateResDetail(request.POST, request.FILES)
        if form.is_valid():
            restourant = Restourant_detail()
            restourant.title_uz = form.cleaned_data.get('title_uz')
            restourant.title_en = form.cleaned_data.get('title_en')
            restourant.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                restourant.image = request.FILES['image']
            restourant.description_uz = form.cleaned_data.get('description_uz')
            restourant.description_en = form.cleaned_data.get('description_en')
            restourant.description_ru = form.cleaned_data.get('description_ru')
            restourant.save()
            return redirect('update_resdetail')
    form = CreateResDetail()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'restourant_detail/create_restourant.html', context)

def update_resdetail(request):
    resdetail = Restourant_detail.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'resdetail': resdetail,
        'admin': admin,
    }

    return render(request, 'restourant_detail/update_resdetail.html', context)


def edit_resdetail(request, id):
    admin = Creator.objects.get(user=request.user)
    resdetail = Restourant_detail.objects.get(pk=id)
    if request.method == 'POST':
        form = EditResDetail(request.POST, request.FILES, instance=resdetail)
        if request.FILES:
            resdetail.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_resdetail')
    else:
        form = EditResDetail(instance=resdetail)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'restourant_detail/edit_restourant_detail.html', context)


def resdetail_delate(request, id):
    resdetail = Restourant_detail.objects.get(pk=id)
    resdetail.delete()
    return redirect('update_resdetail')
#################################################################################################################
#################################################################################################################
#################################### BUSSINES DETAIL BO'LIMI ####################################################

def create_bussines_detail(request):
    if request.method == 'POST':
        form = CreateBussinesDetail(request.POST, request.FILES)
        if form.is_valid():
            bussinesdet = Bussiness_detail()
            bussinesdet.title_uz = form.cleaned_data.get('title_uz')
            bussinesdet.title_en = form.cleaned_data.get('title_en')
            bussinesdet.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                bussinesdet.image = request.FILES['image']
            bussinesdet.description_uz = form.cleaned_data.get('description_uz')
            bussinesdet.description_en = form.cleaned_data.get('description_en')
            bussinesdet.description_ru = form.cleaned_data.get('description_ru')
            bussinesdet.save()
            return redirect('update_bussinesdet')
    form = CreateBussinesDetail()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'bussiness_detail/create_bussines_detail.html', context)

def update_bussinesdet(request):
    bussinesupdate = Bussiness_detail.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'bussinesupdate': bussinesupdate,
        'admin': admin,
    }

    return render(request, 'bussiness_detail/update_bussines_detail.html', context)

def edit_bussinesdet(request, id):
    admin = Creator.objects.get(user=request.user)
    bussinesdet = Bussiness_detail.objects.get(pk=id)
    if request.method == 'POST':
        form = EditBussinesDetail(request.POST, request.FILES, instance=bussinesdet)
        if request.FILES:
            bussinesdet.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_bussinesdet')
    else:
        form = EditBussinesDetail(instance=bussinesdet)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'bussiness_detail/edit_bussines_detail.html', context)

def bussinesdet_delate(request, id):
    resdetail = Bussiness_detail.objects.get(pk=id)
    resdetail.delete()
    return redirect('update_bussinesdet')
#################################################################################################################
#################################################################################################################
#################################### SERVICES BO'LIMI ###########################################################
def createservices(request):
    if request.method == 'POST':
        form = CreateServices(request.POST, request.FILES)
        if form.is_valid():
            service = Services()
            service.title_uz = form.cleaned_data.get('title_uz')
            service.title_en = form.cleaned_data.get('title_en')
            service.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                service.image = request.FILES['image']
            service.descriptions_uz = form.cleaned_data.get('descriptions_uz')
            service.descriptions_en = form.cleaned_data.get('descriptions_en')
            service.descriptions_ru = form.cleaned_data.get('descriptions_ru')
            service.save()
            return redirect('services_update')
    form = CreateServices()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'services/add_services.html', context)







def services_update(request):
    service = Services.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    paginator = Paginator(service, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        service = paginator.page(page)
    except PageNotAnInteger:
        service = paginator.page(1)
    except EmptyPage:
        service = paginator.page(paginator.num_pages)
    context = {
        'service': service,
        'admin': admin,
        'page':page,
    }

    return render(request, 'services/services_update.html', context)



def services_edit(request, id):
    admin = Creator.objects.get(user=request.user)
    service = Services.objects.get(pk=id)
    if request.method == 'POST':
        form = EditServices(request.POST, request.FILES, instance=service)
        if request.FILES:
            service.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('services_update')
    else:
        form = EditServices(instance=service)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'services/services_edit.html', context)



def services_delate(request, id):
    service = Services.objects.get(pk=id)
    service.delete()
    return redirect('services_update')
#################################################################################################################
#################################################################################################################
#################################### ABOUTUS BO'LIMI ############################################################
def createabout(request):
    if request.method == 'POST':
        form = CreateAbout(request.POST, request.FILES)
        if form.is_valid():
            about = Aboutus()
            about.title_uz = form.cleaned_data.get('title_uz')
            about.title_en = form.cleaned_data.get('title_en')
            about.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                about.image = request.FILES['image']
            about.descriptions_uz = form.cleaned_data.get('descriptions_uz')
            about.descriptions_en = form.cleaned_data.get('descriptions_en')
            about.descriptions_ru = form.cleaned_data.get('descriptions_ru')
            about.save()
            return redirect('about_update')
    form = CreateAbout()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'aboutus/add_aboutus.html', context)

def about_update(request):
    about = Aboutus.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    context = {
        'about': about,
        'admin': admin,
    }
    return render(request, 'aboutus/about_update.html', context)



def about_edit(request, id):
    admin = Creator.objects.get(user=request.user)
    about = Aboutus.objects.get(pk=id)
    if request.method == 'POST':
        form = EditAbout(request.POST, request.FILES, instance=about)
        if request.FILES:
            about.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('about_update')
    else:
        form = EditAbout(instance=about)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'aboutus/about_edit.html', context)


def about_delate(request, id):
    about = Aboutus.objects.get(pk=id)
    about.delete()
    return redirect('about_update')
#################################################################################################################
#################################################################################################################
#################################### SLIDER BO'LIMI #############################################################
def createslider(request):
    if request.method == 'POST':
        form = CreateSlider(request.POST, request.FILES)
        if form.is_valid():
            slider = Slider()
            slider.title_uz = form.cleaned_data.get('title_uz')
            slider.title_en = form.cleaned_data.get('title_en')
            slider.title_ru = form.cleaned_data.get('title_ru')
            if request.FILES:
                slider.image = request.FILES['image']
            slider.save()
            return redirect('update_slider')
    form = CreateSlider()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'slider/addSlider.html', context)

def update_slider(request):
    slider = Slider.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    paginator = Paginator(slider, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        slider = paginator.page(page)
    except PageNotAnInteger:
        slider = paginator.page(1)
    except EmptyPage:
        slider = paginator.page(paginator.num_pages)
    context = {
        'page':page,
        'slider': slider,
        'admin': admin,
    }
    return render(request, 'slider/update_slider.html', context)


def edit_slider(request, id):
    admin = Creator.objects.get(user=request.user)
    slider = Slider.objects.get(pk=id)
    if request.method == 'POST':
        form = EditSlider(request.POST, request.FILES, instance=slider)
        if request.FILES:
            slider.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_slider')
    else:
        form = EditSlider(instance=slider)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'slider/edit_slider.html', context)

def delate_slider(request, id):
    slider = Slider.objects.get(pk=id)
    slider.delete()
    return redirect('update_slider')
#################################################################################################################
#################################################################################################################
#################################### ROOM IMAGE BO'LIMI #########################################################
def createroomslider(request):
    if request.method == 'POST':
        form = RoomSlider(request.POST, request.FILES)
        if form.is_valid():
            roomslider = Images()
            roomslider.room = form.cleaned_data.get('room')
            if request.FILES:
                roomslider.image = request.FILES['image']
            roomslider.save()
            return redirect('update_roomsss_slider')
    form = RoomSlider()
    admin = Creator.objects.get(user=request.user)
    context = {
        'form': form,
        'admin': admin,
    }
    return render(request, 'roomslider/RoomSlider.html', context)

def update_roomsss_slider(request):
    room = Rooms.objects.all()
    roomslider = Images.objects.all().order_by('id')
    admin = Creator.objects.get(user=request.user)
    paginator = Paginator(roomslider, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        roomslider = paginator.page(page)
    except PageNotAnInteger:
        roomslider = paginator.page(1)
    except EmptyPage:
        roomslider = paginator.page(paginator.num_pages)
    context = {
        'page':page,
        'roomslider': roomslider,
        'admin': admin,
        'room':room,
    }
    return render(request, 'roomslider/rooms_lider.html', context)



def edit_roomsliders(request, id):
    admin = Creator.objects.get(user=request.user)
    room_slider = Images.objects.get(pk=id)
    if request.method == 'POST':
        form = EditRoomSlider(request.POST, request.FILES, instance=room_slider)
        if request.FILES:
            room_slider.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect('update_roomsss_slider')
    else:
        form = EditRoomSlider(instance=room_slider)
        context = {'form': form,
                   'admin':admin,}

        return render(request, 'roomslider/edit_roomssliders.html', context)

def delate_roomssliders(request, id):
    roomsliders = Images.objects.get(pk=id)
    roomsliders.delete()
    return redirect('update_roomsss_slider')

#################################################################################################################
#################################################################################################################
#################################### REGISTRATIONS BO'LIMI ######################################################
def order_detail_reg(request):
    info = Informations.objects.all().order_by('id')
    roomlist = Rooms.objects.all().order_by('id')
    roomcategory = Category.objects.all().order_by('id')
    orderdetail = Order.objects.all().order_by('id')
    paginator = Paginator(orderdetail, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        orderdetail = paginator.page(page)
    except PageNotAnInteger:
        orderdetail = paginator.page(1)
    except EmptyPage:
        orderdetail = paginator.page(paginator.num_pages)
    user = Registration.objects.get(user=request.user)
    context = {
        'info': info,
        'roomlist': roomlist,
        'roomcategory': roomcategory,
        'orderdetail': orderdetail,
        'user': user,
        'page':page,
    }
    return render(request, 'registration/reg_orderlist.html', context)

def admin_note_reg(request, id):
    order = Order.objects.get(pk=id)
    user = Registration.objects.get(user=request.user)
    if request.method == 'POST':
        form = RegNoteForm(request.POST,  instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail_reg')
    else:
        form = RegNoteForm(instance=order)
        context = {'form': form,
                'user': user,
                'order':order,
                  }

        return render(request, 'registration/admin_note_reg.html', context)



def order_delate_reg(request, id):
    orders = Order.objects.get(pk=id)
    orders.delete()
    return redirect('order_detail_reg')


#################################################################################################################
#################################################################################################################
#################################### REGISTRATION CONTACT BO'LIMI ###############################################


def contact_messages_reg(request):
    contact = ContactMessage.objects.all().order_by('id')
    paginator = Paginator(contact, 3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        contact = paginator.page(page)
    except PageNotAnInteger:
        contact = paginator.page(1)
    except EmptyPage:
        contact = paginator.page(paginator.num_pages)
    user = Registration.objects.get(user=request.user)
    context = {
        'contact': contact,
        'user': user,
        'page':page,
    }

    return render(request, 'registration/contact_registration.html', context)


def status_contact_reg(request, id):
    contact = ContactMessage.objects.get(pk=id)
    user = Registration.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditContactReg(request.POST,  instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_messages_reg')
    else:
        form = EditContactReg(instance=contact)
        context = {'form': form,
                'user': user,
                'order':contact,
                  }

        return render(request, 'registration/contact_status_reg.html', context)

def contact_delate_reg(request, id,):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_messages_reg')
#################################################################################################################
#################################################################################################################
#################################### TARJIMA BO'LIMI ############################################################

def selectlanguagess(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        #return HttpResponse(lang)
        return redirect('creatoradmin')


def selectlanguagee(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl= request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        #return HttpResponse(lang)
        return redirect('registration')



