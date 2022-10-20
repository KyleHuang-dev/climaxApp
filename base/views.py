from django.shortcuts import render, redirect
from .models import City, Climax
from .forms import ClimaxForm


# Create your views here.


def home(request):
    city = City.objects.all()
    climaxs = Climax.objects.all()
    
    context = {
        'city' : city,
        'climaxs': climaxs}
    return render(request, 'base/home.html', context)


def climax(request, pk):
    climaxs = Climax.objects.filter(city__name__icontains = pk)
    
    context = {'climaxs': climaxs}
    return render(request, 'base/climax.html', context)
 

def createClimax(request):
    form = ClimaxForm()

    if request.method == 'POST':
        form = ClimaxForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form' : form}
    return render(request, 'base/climaxForm.html', context)

    
def updateClimax(request, pk):
    climax = Climax.objects.get(id = pk)
    form = ClimaxForm(instance = climax)

    if request.method == 'POST':
        form= ClimaxForm(request.POST, instance= climax)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form' : form }
    return render(request, 'base/climaxForm.html', context)


def deleteClimax(request, pk):
    climax = Climax.objects.get( id = pk )

    if request.method == 'POST':
        climax.delete()
        return redirect('home')

    context = f"{climax.city} {climax.date} at {climax.temperature}"
    return render(request, 'base/deleteForm.html', {'obj': context})
    