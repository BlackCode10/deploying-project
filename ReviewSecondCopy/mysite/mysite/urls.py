from django.contrib import admin
from django.conf.urls import url, include
from Registration import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^registration/', include('Registration.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/', views.special, name='special'),
]