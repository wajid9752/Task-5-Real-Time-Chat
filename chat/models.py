from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Room(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name = "MyRooms")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Message(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name = "Mymsg")
    room = models.ForeignKey(Room , on_delete=models.CASCADE , related_name="rooms")
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message +" by....."+ self.user.username 