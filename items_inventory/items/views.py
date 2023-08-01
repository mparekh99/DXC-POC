"""
Views.py
"""

import json
from pathlib import Path
import os
import os.path
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import *
from .models import *

def upload_file(request):
    """Uploading File function"""
    context = {}
    if request.method == "POST":
       uploaded_file = request.FILES['Inventory']
       fs = FileSystemStorage()
    #    uploaded_file.name = 'Inventory.json'
       name = fs.save(uploaded_file.name, uploaded_file)
       #os.rename(uploaded_file.name, "Inventory.json")

       context['url'] = fs.url(name)

    # index(request)

    return render(request, "upload.html", context)

def index(request):
    """Homepage display"""

    mystock = Item.objects.all().values() 
    template = loader.get_template('index.html')
    print(FileSystemStorage.path)
    source_dir = Path("C:/Users/mparekh9/OneDrive - DXC" + \
                      " Production/Documents/Repos/WebApp_Practice/items_inventory/media/")
    files = source_dir.glob("*.json")
    print(files)
    #print(len(files))

    if not mystock: #it is empty
        count = 0
    else:
        count = getattr(Item.objects.last(), "id") + 1

    #print(getattr(Item.objects.last(), "name"))

    for file in files:
        #print("Hello")
        with file.open('r') as file_handle:
            data = json.load(file_handle)

            for i in data['items']:
                name = i['name']
                expiration = i['sell_in']
                quality = i['quality']
                x = Item(count, name, expiration, quality)
                x.save()
                count =  count + 1
            print("Mihir")
            mystock = Item.objects.all().values()
        print("Removing")
        os.remove(file)
        print("Removed")
    
    print("Finishd")
    context = {
        'mystock': mystock
    }

    return HttpResponse(template.render(context, request))


def add(request):
    """Add page """
    template = loader.get_template('add_item.html')
    return HttpResponse(template.render({}, request))

def addItem(request):
    """Adding function"""
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = addForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            name = request.POST['name']
            expiraiton = request.POST['expiration']
            quality = request.POST['quality']

            print(name, expiraiton, quality)

            if Item.objects.last():
                ID = getattr(Item.objects.last(), "id") + 1
            else:
                ID = 0


            new_item = Item(ID, name, expiraiton, quality)
            new_item.save()       
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addForm()

    print("Missed Function")
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    """Update page"""
    item = Item.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'updated_item': item,
    }
    return HttpResponse(template.render(context, request))

def updateItem(request, id):
    """updating funciton"""
    name = request.POST['name']
    expiraiton = request.POST['expiration']
    quality = request.POST['quality']

    item = Item.objects.get(id=id)
    item.name = name
    item.expiration = expiraiton
    item.quality = quality
    item.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    """Deleting an item"""
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('index'))

def deleteAll(request):
    """Deleting all items"""
    for item in Item.objects.all():
        item.delete()
    return HttpResponseRedirect(reverse('index'))

def projectedData(request):
    """Projected data function"""
    inventory = []

    # Fill up inventory with item objects

    for item in Item.objects.all():
        name = getattr(item, "name")
        expiration = getattr(item, "expiration")
        quality = getattr(item, "quality")
        inventory.append(kata_item(name, expiration, quality))    


    if request.method == 'POST':

        form = NameForm(request.POST)
        if form.is_valid():
            print(request.POST)   
            days = int(form.cleaned_data['numDays'])

            for day in range(days):
                #print("Hello")
                GildedRose(inventory).update_quality()
                for item in inventory:
                    print(item)

            #Updated quality is stored in inventory
            count = 0

            for item in Item.objects.all():
                updated_expiration= inventory[count].sell_in
                updated_quality= inventory[count].quality
                setattr(item, 'expiration', updated_expiration)
                setattr(item, 'quality', updated_quality)
                item.save()
                 #adds to database
                count = count + 1


            print(days)

            return HttpResponseRedirect(reverse('index'))
    else:
        form = NameForm()

    return HttpResponseRedirect(reverse('index'))
