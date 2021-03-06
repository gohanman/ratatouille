# -*- coding: utf-8; mode: python -*-
"""
Custom email profiles
"""

from __future__ import unicode_literals, absolute_import

from rattail.mail import Email

# bring in some common ones from rattail
from rattail.emails import datasync_error_watcher_get_changes, filemon_action_error


class rattail_import_sample_updates(Email):
    """
    Sent when a Sample -> Ratatouille import involves data changes
    """
    fallback_key = 'rattail_import_updates'
    default_subject = "Changes for Sample -> Ratatouille"
