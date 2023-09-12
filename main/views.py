from django.shortcuts import render
from .models import Item

def homepage(request):
    pokeBalls = Item(
        name = 'Poke Ball',
        amount = 10,
        description = 'A device for catching wild Pokemon.'
    )

    greatBalls = Item(
        name = 'Great Ball',
        amount = 5,
        description = 'A good, high-performance PokeBall.'
    )

    ultraBalls = Item(
        name = 'Ultra Ball',
        amount = 2,
        description = 'An ultra-high performance PokeBall.'
    )

    pokeBallsPocket = {
        'pokeBalls' : pokeBalls,
        'greatBalls' : greatBalls,
        'ultraBalls' : ultraBalls
    }

    potion = Item(
        name = 'Potion',
        amount = 5,
        description = 'It restores the HP of one Pokemon by 20 points.'
    )

    superPotion = Item(
        name = 'Super Potion',
        amount = 3,
        description = 'It restores the HP of one Pokemon by 50 points.'
    )

    hyperPotion = Item(
        name = 'Hyper Potion',
        amount = 2,
        description = 'It restores the HP of one Pokemon by 200 points.'
    )

    medicinesPocket = {
        'potion' : potion,
        'superPotion' : superPotion,
        'hyperPotion' : hyperPotion
    }

    return render(request, "main.html", {'pokeBallsPocket' : pokeBallsPocket, 'medicinesPocket' : medicinesPocket})

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
def about(request):
    return render(request, "about.html")