from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
import uuid
from .models import Room , Message
from django.contrib.auth.models import User
from .forms import RegisterUserForm




def register_view(request):
    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
           form.save()
           userName = request.POST.get('username')
           pWord = request.POST.get('password1')
           
           user = authenticate(request, username=userName, password=pWord)
           if user is not None:
            login(request, user)
            messages.success(request , "You are Registerd Successfully ! Welcome to Home")
            return redirect('home')
        return render(request , "chat/register.html",{'form':form})
        

    return render(request , "chat/register.html",{'form':RegisterUserForm()} )    

def login_view(request):
    if request.POST:
        userName = request.POST.get('username')
        pWord = request.POST.get('password')
        
        user = authenticate(request, username=userName, password=pWord)
        
        if user is not None:
            login(request, user)
            messages.success(request , "You are Logged In Successfully ! Welcome to Home")
            return redirect('home')
        else:
            return redirect('login')
    return render(request , "chat/login.html" )    



def logout_view(request):
    logout(request)
    return redirect("login")
  
 
@login_required(login_url="login")  
def lobby(request):
    context={}
    query = request.GET.get('query')
    if query != None:
       matched_rooms = Room.objects.filter(name__icontains = query )
       context['matched_rooms'] = matched_rooms
       
    context['rooms'] = Room.objects.filter(user=request.user)
    print(context)
    return render(request, 'chat/lobby.html' ,context)



@login_required(login_url="login")  
def create_room(request):
    if request.POST:
      room_name = request.POST['room_name']

      if Room.objects.filter(name=room_name).exists():
          messages.success(request ,"Room name already registerd")
          return redirect("create-room")
      
      else:
          new_room = Room.objects.create(name=room_name , user = request.user)
          new_room.save()
          return redirect('chat-view' , new_room.id)

    return render(request , "chat/create-room.html")  


@login_required(login_url="login")  
def chat_view(request , pk):
   room = Room.objects.get(id=pk)
   messages = room.rooms.all()
   print(messages)
   return render(request , "chat/chat-view.html" , {'room': room , 'old_messages':messages})


@login_required(login_url="login")  
def delete_room(request , pk):
   room = Room.objects.get(id=pk)
   room.delete()
   messages.success(request , "Delete Successfully")
   return redirect("home")