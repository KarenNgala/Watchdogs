from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$', views.home, name='home'),
    url('register/', views.register, name='register'),
    url('profile/', views.profile, name='profile'),
    url('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),    
    url(r'^business/', views.business, name='business'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)