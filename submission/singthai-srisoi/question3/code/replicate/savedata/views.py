from django.shortcuts import render, redirect
from .forms import MealForm
from .models import Meal
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            meal = Meal(name=name, quantity=quantity)
            # save into both databases
            saveObj(meal)
            # redirect
            return redirect('index')
    else:
        form = MealForm()   
    context = {'form': form}
    return render(request, 'index.html', context)

def mealList(request):
    meals_mongo = Meal.objects.using('mongodb').all().order_by('-datetime')
    meals = Meal.objects.all().order_by('-datetime')
    context = {'meals': meals, 'meals_mongo': meals_mongo}
    return render(request, 'meals.html', context)

def saveObj(meal):
    meal.save()
    meal.save(using='mongodb')

