from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$' , include('login.urls')),
    url('^business/' , include('business.urls')),
    url('^discover/' , include('discover.urls')),
    url('^groups/' , include('groups.urls')),
    url('^messages/' , include('vmessages.urls')),
    url('^notifications/' , include('notifications.urls')),
    url('^settings/' , include('settings.urls')),
    url('^signup/' , include('signup.urls')),
    url('^uprofile/' , include('uprofile.urls')),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
