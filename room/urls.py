from django.urls import path
from room import views
urlpatterns = [
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]