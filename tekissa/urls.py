from . import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from index.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('shop/', include('shop.urls')),
    path('', include('index.urls')),
    path('', homepage, name="index"),
    #path('__debug__', include('debug_toolbar.urls')),
]
if settings.DEBUG:
    # urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
