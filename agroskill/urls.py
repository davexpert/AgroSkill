from django.contrib import admin
from django.urls import path
from agrosite.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('fruits', fruits_view, name='fruits_list'),
    path('fruit_detail', fruit_detail_view, name='fruit_ditail'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
