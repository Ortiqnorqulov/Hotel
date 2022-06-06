from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blog.models import Blog
from home.models import FAQ, Informations, Special_offers, Restourant_detail, Bussiness_detail, ContactMessage
from room.models import Category, Rooms, Order, Services, Aboutus, Business, Restourant, Spa, Slider, Images
from .models import CustomUser, Creator, Registration



#####################################################################################################################
#####################################################################################################################
###################################### USER BO'LIMI #################################################################

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'full_name', 'phone', 'password1', 'password2', 'email', 'user_type']

        widgets = {
            'user_type': forms.Select(
                attrs={'class': "form-control"}
            )
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'phone',)
        # widgets = {'user_type': forms.Select(attrs={'class': "form-control"})}



class CreatorUpdateForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['bio', 'country', 'address', 'city', 'image']



class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['bio', 'country', 'address', 'city', 'image']


class AdminNoteForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'surname','phone', 'email', 'guest', 'arrival', 'departure', 'room', 'status', 'ip',)



#####################################################################################################################
#####################################################################################################################
###################################### CATEGORY BO'LIMI #############################################################


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [ 'title_uz', 'title_en', 'title_ru', 'description_uz', 'description_en', 'description_ru', 'image',  'slug', 'status']



class CategoryEdit(forms.ModelForm):
    class Meta:
        model = Category
        fields = ( 'title_uz', 'title_en', 'title_ru', 'description_uz', 'description_en','description_ru',  'image', 'status', 'slug',)


#####################################################################################################################
#####################################################################################################################
###################################### ROOM BO'LIMI #################################################################


class AddRoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ( 'title_uz', 'title_en', 'title_ru', 'price_one_uz', 'price_one_en', 'price_one_ru','price_two_uz','price_two_en', 'price_two_ru',   'description_uz', 'description_en', 'description_ru',  'category', 'image', 'status', 'slug',)




class EditRoom(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ( 'title_uz', 'title_en', 'title_ru', 'price_one_uz', 'price_one_en', 'price_one_ru','price_two_uz','price_two_en', 'price_two_ru',   'description_uz', 'description_en', 'description_ru',  'category', 'image', 'status', 'slug',)

#####################################################################################################################
#####################################################################################################################
###################################### FAQ BO'LIMI #################################################@################

class FaqEditForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('ordernumber', 'question_uz', 'question_en', 'question_ru', 'answer_uz', 'answer_en', 'answer_ru', 'status',)


class FaqForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ('ordernumber',  'question_uz', 'question_en', 'question_ru',  'answer_uz', 'answer_en', 'answer_ru', 'status',)
#####################################################################################################################
#####################################################################################################################
###################################### INFO BO'LIMI #################################################################

class AddInfo(forms.ModelForm):
    class Meta:
        model = Informations
        fields = ['title_uz','title_en','title_ru', 'country',  'city', 'address_uz', 'address_en','address_ru', 'phone', 'email', 'image', 'telegram','instagram', 'description_uz','description_en','description_ru', 'status',]


class EditInfo(forms.ModelForm):
    class Meta:
        model = Informations
        fields = ['title_uz','title_en','title_ru', 'country',  'city', 'address_uz', 'address_en','address_ru', 'phone', 'email', 'image', 'telegram', 'description_uz','description_en','description_ru', 'status',]

#####################################################################################################################
#####################################################################################################################
###################################### BLOG BO'LIMI #################################################################
class AddBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title_uz','title_en','title_ru', 'image', 'description_uz','description_en','description_ru', 'status',]


class EditBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title_uz','title_en','title_ru', 'image', 'description_uz','description_en','description_ru', 'status',]

#####################################################################################################################
#####################################################################################################################
###################################### BUSSINESS BO'LIMI ############################################################
class AddBussines(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]


class EditBussines(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]

#####################################################################################################################
#####################################################################################################################
###################################### RESTOURANT BO'LIMI ############################################################

class AddRestourant(forms.ModelForm):
    class Meta:
        model = Restourant
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]


class EditRestourant(forms.ModelForm):
    class Meta:
        model = Restourant
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]

#####################################################################################################################
#####################################################################################################################
###################################### SPA BO'LIMI ##################################################################
class AddSpa(forms.ModelForm):
    class Meta:
        model = Spa
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]


class EditSpa(forms.ModelForm):
    class Meta:
        model = Spa
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]
#####################################################################################################################
#####################################################################################################################
###################################### SPECIAL OFFERS BO'LIMI #######################################################
class AddSpecial(forms.ModelForm):
    class Meta:
        model = Special_offers
        fields = ['title_uz','title_en','title_ru', 'image', 'description_uz','description_en','description_ru',]


class EditSpecial(forms.ModelForm):
    class Meta:
        model = Special_offers
        fields = ['title_uz','title_en','title_ru', 'image', 'description_uz','description_en','description_ru',]


#####################################################################################################################
#####################################################################################################################
###################################### SERVICES BO'LIMI #############################################################
class CreateServices(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title_uz','title_en','title_ru',  'image', 'descriptions_uz','descriptions_en','descriptions_ru',]


class EditServices(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title_uz','title_en','title_ru',  'image', 'descriptions_uz','descriptions_en','descriptions_ru',]
#####################################################################################################################
#####################################################################################################################
###################################### RESTOURANT DETAIL BO'LIMI ####################################################
class CreateResDetail(forms.ModelForm):
    class Meta:
        model = Restourant_detail
        fields = ['title_uz','title_en','title_ru',  'image', 'description_uz','description_en','description_ru',]


class EditResDetail(forms.ModelForm):
    class Meta:
        model = Restourant_detail
        fields = ['title_uz','title_en','title_ru',  'image', 'description_uz','description_en','description_ru',]
#####################################################################################################################
#####################################################################################################################
###################################### BUSSINES DETAIL BO'LIMI ######################################################
class CreateBussinesDetail(forms.ModelForm):
    class Meta:
        model = Bussiness_detail
        fields = ['title_uz','title_en','title_ru',  'image', 'description_uz','description_en','description_ru',]


class EditBussinesDetail(forms.ModelForm):
    class Meta:
        model = Bussiness_detail
        fields = ['title_uz','title_en','title_ru',  'image', 'description_uz','description_en','description_ru',]
#####################################################################################################################
#####################################################################################################################
###################################### ABOUTUS BO'LIMI ##############################################################

class CreateAbout(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]


class EditAbout(forms.ModelForm):
    class Meta:
        model = Aboutus
        fields = ['title_uz','title_en','title_ru', 'image', 'descriptions_uz','descriptions_en','descriptions_ru',]

#####################################################################################################################
#####################################################################################################################
###################################### CONTACTUS BO'LIMI ############################################################
class EditContact(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','phone', 'subject', 'message','status','note',]


#####################################################################################################################
#####################################################################################################################
###################################### REGISTRATION ORDER BO'LIMI ###################################################


class RegNoteForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'surname','phone', 'email', 'guest', 'arrival', 'departure', 'room', 'status', 'ip',)



class EditContactReg(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','phone', 'subject', 'message','status','note',]


#####################################################################################################################
#####################################################################################################################
###################################### SLIDER BO'LIMI ###############################################################
class CreateSlider(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title_uz','title_en','title_ru', 'image',]


class EditSlider(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title_uz','title_en','title_ru', 'image',]



#####################################################################################################################
#####################################################################################################################
###################################### SLIDER BO'LIMI ###############################################################
class RoomSlider(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['room', 'image',]


class EditRoomSlider(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['room', 'image',]
