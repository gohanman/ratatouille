# -*- coding: utf-8; -*-
"""
Recipe Views
"""

from __future__ import unicode_literals, absolute_import

from rattail.db import model
from ratatouille.db.model.core import Recipes

from tailbone.views import MasterView, AutocompleteView


class RecipesView(MasterView):
    """
    Master view for the Recipes class.
    """
    model_class = Recipes
    has_versions = False

    grid_columns = [
        'name',
        'recipe_id',
        'plu',
        'updated',
    ]

    form_fields = [
        'name',
        'recipe_id',
        'plu',
        'updated',
    ]

    def configure_grid(self, g):
        super(RecipesView, self).configure_grid(g)

        # name
        g.filters['name'].default_active = True
        g.filters['name'].default_verb = 'contains'
        g.set_sort_defaults('name')
        g.set_link('name')

class RecipesAutocomplete(AutocompleteView):

    mapped_class = Recipes
    fieldname = 'name'


def includeme(config):

    # autocomplete
    config.add_route('ratatouille.recipes.autocomplete', '/ratatouille/recipes/autocomplete')
    config.add_view(RecipesAutocomplete, route_name='ratatouille.recipes.autocomplete',
                    renderer='json', permission='brands.list')

    RecipesView.defaults(config)
