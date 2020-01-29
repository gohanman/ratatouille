# -*- coding: utf-8; mode: python -*-
"""
Static assets
"""


def includeme(config):
    config.include('tailbone.static')
    config.add_static_view('ratatouille', 'ratatouille.web:static', cache_max_age=3600)
