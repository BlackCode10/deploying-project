from django.conf.urls import url
from Registration import views

app_name = 'Registration'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]