"""定义learning_logs的URL模式"""
from django.conf.urls import url
from learning_logs import views
from django.urls import path
from django.urls import path, re_path

app_name = "learning_logs"
urlpatterns = [
	# home
	path('', views.index, name='index'),
	# topics
	path('topics/', views.topics, name='topics'),
	# path('topics/1/', views.topics, name='topics'),
	re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
	#re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]

