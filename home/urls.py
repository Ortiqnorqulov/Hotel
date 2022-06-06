from django.urls import path
from home import views


urlpatterns = [
    path('IndexPage/', views.IndexPage.as_view(),name='IndexPage'),
    path('InfoPage/', views.InfoPage.as_view(),name='InfoPage'),
    path('ContactUs/', views.ContactUs.as_view(),name='ContactUs'),
    path('RoomsPage/<int:id>/', views.RoomsPage.as_view(),name='RoomsPage'),
    path('RoomDetailPage/<int:id>/<slug:slug>', views.RoomDetailPage.as_view(),name='RoomDetailPage'),
########################################################################################################################
########################################################################################################################
########################################################################################################################
    path('', views.home,name='home'),
    path('special_offers/<int:id>', views.special_offers, name='special_offers'),
    #################### SERVISLAR ##############################
    path('services/', views.services,name='services'),
    path('bussines_detail/', views.bussines_detail,name='bussines_detail'),
    path('restourant_detail/', views.restourant_detail,name='restourant_detail'),
    path('gallery/', views.gallery,name='gallery'),
    #############################################################
    path('aboutus/', views.aboutus,name='aboutus'),
    path('aboutus_detail/<int:id>', views.aboutus_detail, name='aboutus_detail'),

    path('contactus/',views.contactus, name='contactus'),
    path('faq/', views.faq, name='faq'),
    path('room/<int:id>/<slug:slug>', views.room_detail, name='room_detail'),
    path('category/<int:id>/<slug:slug>',views.category_room, name='category_room'),
]