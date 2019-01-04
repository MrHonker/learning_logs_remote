"""定义learning_logs的URL模式"""
from django.conf.urls import url
from learning_logs import views
from django.urls import path

app_name = "learning_logs"
urlpatterns = [
	# home
	path('', views.index, name='index'),
	# topics
	path('topics/', views.topics, name='topics'),

]

