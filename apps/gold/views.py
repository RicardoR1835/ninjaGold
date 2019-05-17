# gold app views
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.sessions.models import Session
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'msg' not in request.session:
        request.session['msg'] = []
    return render(request, "gold/index.html")

def farm(request):
    x = random.randint(10,20)
    print(x)
    print('in the farm')
    request.session['gold'] += x
    request.session['msg'].insert(0, '<p class="sp" style="color: green"> Earned ' + str(x) + ' gold pieces from the farm!</p>')
    return redirect('/')

def cave(request):
    x = random.randint(5,10)
    print('in the cave')
    print(x)
    request.session['gold'] += x
    request.session['msg'].insert(0, '<p class="sp" style="color: green"> Earned ' + str(x) + ' gold pieces from the farm!</p>')
    return redirect('/')

def house(request):
    x = random.randint(2,5)
    print('in the house')
    print(x)
    request.session['gold'] += x
    request.session['msg'].insert(0, '<p class="sp" style="color: green"> Earned ' + str(x) + ' gold pieces from the farm!</p>')
    return redirect('/')

def casino(request):
    x = random.randint(-50,50)
    print('in the casino')
    print(x)
    request.session['gold'] += x
    if x > 0:
        request.session['msg'].insert(0, '<p class="sp" style="color: green"> Earned ' + str(x) + ' gold pieces from the casino!</p>')
    elif x < 0:
        request.session['msg'].insert(0, '<p class="sp" style="color: red"> Yikes! Lost ' + str(x) + ' gold pieces from the cave!</p>')
    return redirect('/')