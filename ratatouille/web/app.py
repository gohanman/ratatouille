# -*- coding: utf-8; mode: python; -*-
"""
Ratatouille web app
"""

from __future__ import unicode_literals, absolute_import

from tailbone import app


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    # prefer Ratatouille templates over Tailbone
    settings.setdefault('mako.directories', ['ratatouille.web:templates',
                                             'tailbone:templates',])

    # for graceful handling of postgres restart
    settings.setdefault('retry.attempts', 2)

    # make config objects
    rattail_config = app.make_rattail_config(settings)
    pyramid_config = app.make_pyramid_config(settings)

    # bring in the rest of Ratatouille
    pyramid_config.include('ratatouille.web.static')
    pyramid_config.include('ratatouille.web.subscribers')
    pyramid_config.include('ratatouille.web.views')

    # for graceful handling of postgres restart
    pyramid_config.add_tween('tailbone.tweens.sqlerror_tween_factory',
                             under='pyramid_tm.tm_tween_factory')

    return pyramid_config.make_wsgi_app()
