# -*- coding: utf-8; mode: python; -*-
"""
Views
"""

from __future__ import unicode_literals, absolute_import


def includeme(config):

    # core views
    config.include('ratatouille.web.views.common')
    config.include('ratatouille.web.views.recipes')
    config.include('tailbone.views.auth')
    config.include('tailbone.views.tables')
    config.include('tailbone.views.upgrades')
    config.include('tailbone.views.progress')

    # main table views
    config.include('tailbone.views.brands')
    config.include('tailbone.views.customers')
    config.include('tailbone.views.customergroups')
    config.include('tailbone.views.datasync')
    config.include('tailbone.views.departments')
    config.include('tailbone.views.email')
    config.include('tailbone.views.employees')
    config.include('tailbone.views.messages')
    config.include('tailbone.views.people')
    config.include('tailbone.views.products')
    config.include('tailbone.views.reportcodes')
    config.include('tailbone.views.roles')
    config.include('tailbone.views.settings')
    config.include('tailbone.views.shifts')
    config.include('tailbone.views.stores')
    config.include('tailbone.views.subdepartments')
    config.include('tailbone.views.users')
    config.include('tailbone.views.vendors')

    # batch views
    config.include('tailbone.views.handheld')
    config.include('tailbone.views.inventory')
