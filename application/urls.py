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
    url('all-hoods/',views.neighbourhoods,name='hood'),
    url('new-hood/', views.create_neighbourhood, name='new-hood'),
    url('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
    url('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
    url('single_hood/<hood_id>', views.single_neighbourhood, name='single-hood'),
    url(r'^accounts/register/complete/$', views.join, name='complete'),
    url(r'^join/(\d+)/$', views.join_btn, name='join'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)