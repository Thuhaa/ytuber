from django.urls import path
from . import views
urlpatterns = [
path('', views.homepage_view, name="homepage"),
path('get-video/', views.get_video_view, name='get-video')
]