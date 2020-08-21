from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^accounts/register/complete/$', views.join, name='complete'),
    url(r'^join/(\d+)/$', views.join_btn, name='join'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)