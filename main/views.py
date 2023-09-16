from django.shortcuts import render
from .models import Item
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# def homepage(request):
#     items = Item.objects.all()
#     pokeBalls = Item(
#         name = 'Poke Ball',
#         amount = 10,
#         description = 'A device for catching wild Pokemon.'
#     )

#     greatBalls = Item(
#         name = 'Great Ball',
#         amount = 5,
#         description = 'A good, high-performance PokeBall.'
#     )

#     ultraBalls = Item(
#         name = 'Ultra Ball',
#         amount = 2,
#         description = 'An ultra-high performance PokeBall.'
#     )

#     pokeBallsPocket = {
#         'pokeBalls' : pokeBalls,
#         'greatBalls' : greatBalls,
#         'ultraBalls' : ultraBalls
#     }

#     potion = Item(
#         name = 'Potion',
#         amount = 5,
#         description = 'It restores the HP of one Pokemon by 20 points.'
#     )

#     superPotion = Item(
#         name = 'Super Potion',
#         amount = 3,
#         description = 'It restores the HP of one Pokemon by 50 points.'
#     )

#     hyperPotion = Item(
#         name = 'Hyper Potion',
#         amount = 2,
#         description = 'It restores the HP of one Pokemon by 200 points.'
#     )

#     medicinesPocket = {
#         'potion' : potion,
#         'superPotion' : superPotion,
#         'hyperPotion' : hyperPotion
#     }

#     return render(request, "main.html", {'pokeBallsPocket' : pokeBallsPocket, 'medicinesPocket' : medicinesPocket})

def homepage(request):
    items = Item.objects.all()
    context = {
        'name' : 'Tegar Wahyu Khisbulloh',
        'class' : 'PBP F',
        'items': items
        }
    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:homepage'))

    context = {'form': form}
    return render(request, "add_item.html", context)

def clear_items(request):
    Item.objects.all().delete()
    return HttpResponseRedirect(reverse('main:homepage'))

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