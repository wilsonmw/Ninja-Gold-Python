from django.shortcuts import render, redirect
from random import randint

# Create your views here.
def index(request):
    try:
        request.session["gold"]
    except:
        request.session["gold"]=0
    try:
        request.session["things_done"]
    except:
        request.session["things_done"]=[]
    return render(request, 'ninja_gold_app/index.html')

def process(request):
    if request.POST['spot']=='farm':
        newgold = randint(10,20)
        request.session["gold"]+= newgold
        request.session["things_done"].append("You robbed a farm and stole " + str(newgold) + " gold")
        return redirect('/')
    elif request.POST['spot']=='cave':
        newgold = randint(5,10)
        request.session["gold"]+= newgold
        request.session["things_done"].append("You robbed a cave and stole " + str(newgold) + " gold")
        return redirect('/')
    elif request.POST['spot']=='house':
        newgold = randint(2,5)
        request.session["gold"]+= newgold
        request.session["things_done"].append("You robbed a house and stole " + str(newgold) + " gold")
        return redirect('/')
    elif request.POST['spot']=='casino':
        winlose = randint(1,2)
        print winlose
        if winlose == 1:
            newgold = randint(100,1000)
            request.session["gold"]+= newgold
            request.session["things_done"].append("You won at the casino and won " + str(newgold) + " gold")
            return redirect('/')
        elif winlose == 2:
            newgold = randint(100,1000)
            request.session["gold"]-= newgold
            request.session["things_done"].append("You lost at the casino and lost " + str(newgold) + " gold")
            return redirect('/')


def reset(request):
    request.session["gold"]=0
    request.session["things_done"]=[]
    return redirect('/')

