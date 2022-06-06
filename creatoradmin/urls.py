from django.urls import path
from creatoradmin import views


urlpatterns = [
    ###################### USERLARGA TEGISHLI BO'LIM ###################
    path('register/', views.register, name='register'),
    path('login/', views.login_form, name='login_form'),
    path('logout_form/', views.logout_form, name='logout_form'),
    path('user_update/', views.user_update, name='user_update'),
    path('user_password/', views.user_password, name='user_password'),
    path('CreatorUpdateView/', views.CreatorUpdateView.as_view(), name='CreatorUpdateView'),
    path('RegistrationUpdateView/', views.RegistrationUpdateView.as_view(), name='RegistrationUpdateView'),
    ###################### USER TYPE BO'LIM ############################
    path('registration/', views.registration, name='registration'),
    path('creatoradmin/', views.creatoradmin, name='creatoradmin'),
    ###################### CATEGO'RYALAR BO'LIMI ########################
    path('createcategory/', views.createcategory, name='createcategory'),
    path('category_update/', views.category_update, name ='category_update'),
    path('category_edit/<int:id>/<slug:slug>', views.category_edit, name ='category_edit'),
    path('category_delate/<int:id>/<slug:slug>', views.category_delate, name ='category_delate'),
    #################### HONALAR BO'LIMI ###### #########################
    path('createroom/', views.createroom, name='createroom'),
    path('room_update/', views.room_update, name ='room_update'),
    path('room_edit/<int:id>/<slug:slug>', views.room_edit, name = 'room_edit'),
    path('room_delate/<int:id>/<slug:slug>', views.room_delate, name = 'room_delate'),
    #################### ORDERLAR BO'LIMI ###############################
    path('orderdetail/', views.orderdetail, name='orderdetail'),
    path('admin_note/<int:id>', views.admin_note, name='admin_note'),
    path('order_delate/<int:id>', views.order_delate, name='order_delate'),
    ######################## FAQ BOLIMI ################################
    path('faqs/', views.faqs, name ='faqs'),
    path('faq_update/', views.faq_update, name ='faq_update'),
    path('faq_edit/<int:id>', views.faq_edit, name='faq_edit'),
    path('faq_delate/<int:id>', views.faq_delate, name='faq_delate'),
    ######################## COMMENT BOLIMI #############################
    path('comment/', views.comment, name ='comment'),
    path('comment_delate/<int:id>', views.comment_delate, name='comment_delate'),
    ######################## CONTACT BOLIMI #############################
    path('contact_messages/', views.contact_messages, name ='contact_messages'),
    path('contact_delate/<int:id>', views.contact_delate, name='contact_delate'),
    path('status_contact/<int:id>', views.status_contact, name='status_contact'),
    ######################## INFORMATIONS BOLIMI ########################
    path('createinfo/', views.createinfo, name ='createinfo'),
    path('info_update/', views.info_update, name ='info_update'),
    path('info_edit/<int:id>', views.info_edit, name = 'info_edit'),
    path('info_delate/<int:id>', views.info_delate, name='info_delate'),
    ######################## BLO'G BOLIMI ###############################
    path('createblog/', views.createblog, name ='createblog'),
    path('blog_update/', views.blog_update, name ='blog_update'),
    path('blog_edit/<int:id>', views.blog_edit, name = 'blog_edit'),
    path('blog_delate/<int:id>', views.blog_delate, name='blog_delate'),
    ######################## SERVICES BOLIMI #################################
    path('createservices/', views.createservices, name = 'createservices'),
    path('services_update/', views.services_update, name = 'services_update'),
    path('services_edit/<int:id>', views.services_edit, name = 'services_edit'),
    path('services_delate/<int:id>', views.services_delate, name = 'services_delate'),
    ######################## ABOUTUS BOLIMI #################################
    path('createabout/', views.createabout, name = 'createabout'),
    path('about_update/', views.about_update, name = 'about_update'),
    path('about_edit/<int:id>', views.about_edit, name = 'about_edit'),
    path('about_delate/<int:id>', views.about_delate, name = 'about_delate'),
    ######################## BUSSINESS BOLIMI #################################
    path('createbussines/', views.createbussines, name = 'createbussines'),
    path('update_businnes/', views.update_businnes, name = 'update_businnes'),
    path('edit_bussines/<int:id>', views.edit_bussines, name = 'edit_bussines'),
    path('bussines_delete/<int:id>', views.bussines_delete, name = 'bussines_delete'),
    ######################## RESTOURANT BOLIMI #################################
    path('create_restourant/', views.create_restourant, name='create_restourant'),
    path('update_restourant/', views.update_restourant, name='update_restourant'),
    path('edit_restourant/<int:id>', views.edit_restourant, name = 'edit_restourant'),
    path('restourant_delete/<int:id>', views.restourant_delete, name = 'restourant_delete'),
    ######################## SPA BOLIMI ########################################
    path('create_spa/', views.create_spa, name='create_spa'),
    path('update_spa/', views.update_spa, name='update_spa'),
    path('edit_spa/<int:id>', views.edit_spa, name = 'edit_spa'),
    path('spa_delete/<int:id>', views.spa_delete, name = 'spa_delete'),
    ######################## SPECIAL OFFERS BOLIMI #############################
    path('create_special/', views.create_special, name='create_special'),
    path('update_special/', views.update_special, name='update_special'),
    path('edit_special/<int:id>', views.edit_special, name = 'edit_special'),
    path('special_delete/<int:id>', views.special_delete, name = 'special_delete'),
    ######################## RESTOURANT DETAIL OFFERS BOLIMI ####################
    path('create_resdetail/', views.create_resdetail, name='create_resdetail'),
    path('update_resdetail/', views.update_resdetail, name='update_resdetail'),
    path('edit_resdetail/<int:id>', views.edit_resdetail, name = 'edit_resdetail'),
    path('resdetail_delate/<int:id>', views.resdetail_delate, name = 'resdetail_delate'),
    ######################## SLIDER BOLIMI #####################################
    path('createslider/', views.createslider, name='createslider'),
    path('update_slider/', views.update_slider, name='update_slider'),
    path('edit_slider/<int:id>', views.edit_slider, name = 'edit_slider'),
    path('delate_slider/<int:id>', views.delate_slider, name = 'delate_slider'),
    ######################## BUSSINESS DETAIL OFFERS BOLIMI ####################
    path('create_bussines_detail/', views.create_bussines_detail, name='create_bussines_detail'),
    path('update_bussinesdet/', views.update_bussinesdet, name='update_bussinesdet'),
    path('edit_bussinesdet/<int:id>', views.edit_bussinesdet, name = 'edit_bussinesdet'),
    path('bussinesdet_delate/<int:id>', views.bussinesdet_delate, name = 'bussinesdet_delate'),
    ######################## REGISTRATION ORDER DETAILS BOLIMI ##################
    path('order_detail_reg/', views.order_detail_reg, name='order_detail_reg'),
    path('admin_note_reg/<int:id>', views.admin_note_reg, name='admin_note_reg'),
    path('order_delate_reg/<int:id>', views.order_delate_reg, name='order_delate_reg'),
    ######################## REGISTRATION CONTACT  BOLIMI #######################
    path('contact_messages_reg/', views.contact_messages_reg, name ='contact_messages_reg'),
    path('status_contact_reg/<int:id>', views.status_contact_reg, name='status_contact_reg'),
    path('contact_delate_reg/<int:id>', views.contact_delate_reg, name='contact_delate_reg'),
    ######################## ROOM SLIDER BOLIMI ################################
    path('createroomslider/', views.createroomslider, name ='createroomslider'),
    path('update_roomsss_slider/', views.update_roomsss_slider, name='update_roomsss_slider'),
    path('edit_roomsliders/<int:id>', views.edit_roomsliders, name='edit_roomsliders'),
    path('delate_roomssliders/<int:id>', views.delate_roomssliders, name='delate_roomssliders'),
]