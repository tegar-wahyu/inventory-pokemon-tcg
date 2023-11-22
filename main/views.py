import datetime
import json
from django.shortcuts import render
from .models import Item
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from main.forms import ItemForm
from django.urls import reverse 
from django.http import HttpResponse 
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def homepage(request):
    items = Item.objects.filter(user=request.user)
    context = {
        'name' : request.user.username,
        'class' : 'PBP F',
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:homepage")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_item(request):
    form = ItemForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:homepage'))

    context = {'form': form}
    return render(request, "add_item.html", context)

def change_item_amount(request, item_id, amount):
    item = Item.objects.get(id=item_id)

    if item.amount <= 0 and amount == 'decrease':
        return redirect('main:homepage')
    if amount == 'increase':
        item.amount += 1
    elif amount == 'decrease':
        item.amount -= 1
    item.save()
    return redirect('main:homepage')

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('main:homepage')

def show_xml(request):
    data = Item.objects.all() 
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_items_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(id=item_id)
        item.delete()
        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)