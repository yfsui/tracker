from django.shortcuts import render
from tracker.models import Squirrel
from tracker.forms import SquirrelForm
def all(request):
    squirrels = Squirrel.objects.all()
    context = {'squirrels': squirrels}
    return render(request, 'tracker/all.html', context)

def add(request):
    if request.method=="POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:all')
    else:
        form = SquirrelForm()
    context={'form':form}
    return render(request,'tracker/add.html',context)

def update(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        form = SquirrelForm(request.POST,instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect('tracker:all')
    else:
        form = SquirrelForm(instance = squirrel)
    context={'form':form}
    return render(request,'tracker/update.html',context)

def stats(request):
    total = Squirrel.objects.all().count()
    adult = Squirrel.objects.filter(Age = 'Adult').count()
    juvenile = Squirrel.objects.filter(Age = 'Juvenile').count() 
    fur = Squirrel.objects.filter(Primary_Fur_Color='Gray').count()
    location = Squirrel.objects.filter(Location='Above Ground').count()

    context = {'total':total,
    'adult':adult,
    'juvenile' = juvenile,
    'fur':fur,
    'location':location,}
    return render(request,'tracker/stats.html',context)

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {'squirrels':squirrels}
    return render(request, 'tracker/map.html',context)
