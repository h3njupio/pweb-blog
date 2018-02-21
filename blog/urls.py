from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path('post/(?P<pk>\d+)/', views.post_detail, name='post_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
