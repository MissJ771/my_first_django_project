from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    # username = 'miss J'
    date = datetime.datetime.now()
    hour = int(date.strftime("%H"))
    
    msg = "Good "
    
    if hour < 12:
        msg += "Morning"
    elif hour < 16:
        msg += "Afternoon"
    elif hour < 18:
        msg += "Evening"
    else:
        msg += "Night"
        
    greeting = f"{msg}! Miss J"
        
    tasks = [
        {'id':1, "text":'Cook rice and stew', "done":True},
        {"id":2, "text":'Wash clothes', "done":False},
        {"id":3, "text":'Family get together', "done":False},
        {"id":4, "text":'Hit the gym', "done":False},
        {"id":5, "text":'Practice Django', "done":False},
        {"id":6, "text":'Netflix and Chill', "done":False}
    ]
    
    context = {
        'greeting': greeting,
        'tasks': tasks
    }
    
    return render(request, "home.html", context)

def login(request):
    return render(request, "login.html")