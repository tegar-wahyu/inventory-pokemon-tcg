from django.shortcuts import render

def show_main(request):
    context = {
        'card_name': 'VStar Arceus',
        'type': 'Legendary'
    }

    return render(request, "main.html", context)