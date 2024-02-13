import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import AnonymousUser
from .models import Room , Message 
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        message = text_data_json['message']
        room_id = text_data_json['room_id']
        
        obj = Message.objects.create(
            room = Room.objects.get(id=room_id) ,
            message = message ,
            user = self.scope["user"]
        )
        print(obj)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message ,
                'username': self.scope["user"].username if not isinstance(self.scope["user"], AnonymousUser) else "Anonymous",
                'msgof': obj.user.username ,
                'created_at': str(obj.created_at )
            }
        )


        
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        msgof = event['msgof']
        created_at = event['created_at']
        
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'username': username , 
            'msgof':msgof ,
            'created_at': created_at
        }))