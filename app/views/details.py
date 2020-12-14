from django.shortcuts import render

from app.models import Recipe


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)
