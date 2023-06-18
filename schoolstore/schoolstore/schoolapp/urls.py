

from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
app_name='schoolapp'

urlpatterns = [

    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('edit/',views.edit,name='edit'),
    path('register/', views.register, name='register'),
    path('login_request/',views.login_request,name='login_request'),
    path('message/',views.message,name='message'),


]
if settings.DEBUG:
     urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

