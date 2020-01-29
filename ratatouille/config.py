# -*- coding: utf-8; mode: python; -*-
"""
Custom config
"""

from __future__ import unicode_literals, absolute_import

from rattail.config import ConfigExtension


class RatatouilleConfig(ConfigExtension):
    """
    Rattail config extension for Ratatouille
    """
    key = 'ratatouille'

    def configure(self, config):

        # set some default config values
        config.setdefault('rattail.mail', 'emails', 'ratatouille.emails')
        config.setdefault('tailbone', 'menus', 'ratatouille.web.menus')

        config.setdefault('ratatouille', 'ctdb.url', '')
