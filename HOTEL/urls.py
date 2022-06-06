from home import views
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from creatoradmin import views as CreatoradminViews
from creatoradmin import views as RegistrationViews
from django.utils.translation import gettext_lazy as _
from django.views.static import serve

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectlanguagess',    CreatoradminViews.selectlanguagess, name='selectlanguagess'),
    path('selectlanguagee',    RegistrationViews.selectlanguagee, name='selectlanguagee'),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('room/', include('room.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('creatoradmin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
