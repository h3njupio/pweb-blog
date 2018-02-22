from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path('^$', views.video_list, name='list'),
    re_path('^new$', views.video_new, name='new'),
    re_path('^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)