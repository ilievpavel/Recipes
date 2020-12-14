from django.urls import path

from app.views.details import recipe_details
from app.views.index import index
from app.views.recipes import create_recipe, edit_recipe, delete_recipe

urlpatterns = (
    path('', index, name='index'),
    path('create', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', recipe_details, name='recipe details')
)

# •	'/create' - create recipe page
# •	'/edit/:id' - edit recipe page
# •	'/delete/:id' - delete recipe page
# •	'/details/:id' - recipe details page
