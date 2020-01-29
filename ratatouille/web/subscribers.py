# -*- coding: utf-8; mode: python -*-
"""
Pyramid event subscribers
"""

from __future__ import unicode_literals, absolute_import

import ratatouille


def add_ratatouille_to_context(event):
    renderer_globals = event
    renderer_globals['ratatouille'] = ratatouille


def includeme(config):
    config.include('tailbone.subscribers')
    config.add_subscriber(add_ratatouille_to_context, 'pyramid.events.BeforeRender')
