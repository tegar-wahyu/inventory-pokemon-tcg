from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'VStar Arceus',
        'amount': 66,
        'description': 'Legendary Pokemon',
    }

    return render(request, "main.html", context)