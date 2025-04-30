from django.shortcuts import render

def index(request):
    context = {
        "username": "SkyVaultUser",
        "page_title": "Welcome to SkyVault"
    }
    return render(request, 'index.html', context)