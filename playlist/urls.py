from django.urls import path
from .views import DetailList,ListSong

urlpatterns = [
    path('<int:pk>',DetailList.as_view()),
    path('',ListSong.as_view())
]