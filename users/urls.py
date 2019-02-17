from django.conf.urls import url
from django.contrib.auth.views import login
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),


]
