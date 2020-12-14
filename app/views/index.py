from django.shortcuts import render

from app.models import Recipe


def index(request):
    if Recipe.objects.exists():
        context = {
            'recipes': Recipe.objects.all(),
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

