from django.shortcuts import render, redirect

from app.forms.recipes import RecipeForm, RecipeDeleteForm
from app.models import Recipe


def persist_recipe(request, recipe, template_name):
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)

        context = {
            'form': form,
            'recipe': recipe,
        }

        return render(request, f'{template_name}.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
            'recipe': recipe,
        }

        return render(request, f'{template_name}.html', context)


def create_recipe(request):
    recipe = Recipe()
    return persist_recipe(request, recipe, 'create')


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return persist_recipe(request, recipe, 'edit')


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeDeleteForm(instance=recipe)
        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')
