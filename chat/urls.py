from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.lobby , name="home"),
    path('login/' , views.login_view , name="login" ),
    path('register/' , views.register_view , name="register" ),
    path('logout/' , views.logout_view , name="logout" ),
    path('create-room/' , views.create_room , name="create-room" ),
    path('delete-room/<int:pk>/' , views.delete_room , name="delete-room" ),
    path('chat-view/<int:pk>/' , views.chat_view , name="chat-view" ),
]