# -*- coding: utf-8; mode: python; -*-
"""
Common views
"""

from __future__ import unicode_literals, absolute_import

from tailbone.views import common as base

import ratatouille


class CommonView(base.CommonView):

    project_title = "Ratatouille"
    project_version = ratatouille.__version__ + '+dev'


def includeme(config):
    CommonView.defaults(config)
