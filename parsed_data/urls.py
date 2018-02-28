from django.conf.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #re_path('^$', views.),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)