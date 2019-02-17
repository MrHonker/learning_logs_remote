from django.conf.urls import url
from django.contrib.auth.views import login
from django.urls import path
from . import views

# admin Changeme_123  ;用户名和密码

app_name = 'users'
urlpatterns = [
    # 登录页面
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),

]
