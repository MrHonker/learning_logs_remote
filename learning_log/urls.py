"""learning_log URL Configuration
 views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topi
The `urlpatterns` list routes URLs toimport viewscs/http/urls/
Examples:
Function views
    1. Add an import:  from my_app 
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from learning_logs import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # path('', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('learning_logs.urls', namespace='learning_logs')),
    # 主页
    # path('', views.index, name='index'),
    # # 显示所有的主题
    # path('topics/', views.topics, name='topics'),
]



